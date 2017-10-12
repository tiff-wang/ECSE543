from __future__ import division
from matrix import Matrix


m = Matrix()


class Circuit(object): 
	def __init__(self):
		pass

#circuitNetwork is formatted as a tuples of (J, R, E, A)
#methods solves the (AYA^T) * Vn = A(J-YE) formula for Vn 
	def findNodeVoltage(self, circuitNetwork):
		J = circuitNetwork[0]
		R = circuitNetwork[1]
		E = circuitNetwork[2]
		A = circuitNetwork[3]
		Y = [[0 for x in range(len(R))] for y in range(len(R))]
		
		for i in range(len(Y)):
			Y[i][i] = 1/R[i]

		A_transpose = m.matrixTranspose(A)
		
		AYAT = m.matrixMultiplication(m.matrixMultiplication(A, Y), A_transpose)
		b = m.matrixVectorMultiplication(A, m.vectorSubtraction(J, m.matrixVectorMultiplication(Y, E)))

		return m.choleski(AYAT, b)

#circuitNetwork is formatted as a tuples of (J, R, E, A)
#methods solves the (AYA^T) * Vn = A(J-YE) formula for Vn
#this method is meant to solve a N x 2N linear resistive network
	def sparseFindNodeVoltage(self, circuitNetwork):
		J = circuitNetwork[0]
		R = circuitNetwork[1]
		E = circuitNetwork[2]
		A = circuitNetwork[3]
		Y = [[0 for x in range(len(R))] for y in range(len(R))]
		for i in range(len(Y)):
			Y[i][i] = 1/R[i]
		
		b = len(A[0]) - len(A) + 1
		AYAT = m.sparseMatrixMultiplication(A, 0, b, m.sparseMatrixMultiplication(Y, 0, 1, m.matrixTranspose(A), 0, b), 0, b)
		
		vector = m.sparseMatrixVectorMultiplication(A, 0, b, m.vectorSubtraction(J, m.sparseMatrixVectorMultiplication(Y, 0, 1, E)))
		return m.sparseCholeski(AYAT, vector, b-1)

	def findReq(self, N, R):
		self.FDMatrixGenerator(N, R)
		nodeV = self.findNodeVoltage(self.parseCircuit("q2CircuitFile-{0}.txt".format(N)))
		return nodeV[0] * R / (1 - nodeV[0])

	def sparsefindReq(self, N, R):
		self.FDMatrixGenerator(N, R)
		nodeV = self.sparseFindNodeVoltage(self.parseCircuit("q2CircuitFile-{0}.txt".format(N)))
		return nodeV[0] * R / (1 - nodeV[0])

	def parseCircuit(self, filename):
		file = open(filename, "r")
		circuitFile = file.readlines()

		J = map(float, circuitFile[0].split("\n")[0].split(" "))
		R = map(float, circuitFile[1].split("\n")[0].split(" "))
		E = map(float, circuitFile[2].split("\n")[0].split(" "))

		A = []
		for line in circuitFile[4:]:
			A.append(map(float, line.split("\n")[0].split(" ")))

		return (J, R, E, A)

	'''
	N*2N finite definite mesh circuit with R resistance in each mesh. 
	format of the circuit: (N+1) x (2N+1) total nodes 
							4N^2 + 3N total meshes
	
	node numbering convention

	N+1		2N + 2  ... 
	.
	.
	.
	2		N+3		...
	1		N+2 	... 
		
	
	mesh numbering convention 

	N+1	(2N+1) .. 
	(N)	  . 
	.	  .
	.	  .
	(2)	
	2	(N+2) .. 
	(1)			
	1 	(N+1) 	N+2

	incidence matrix current flow convention: 
		-1 : flowing in 
		 1 : flowing out

	'''


	def FDMatrixGenerator(self, N, res):
		file = open("q2CircuitFile-{0}.txt".format(N), 'w')
		
		node = (N+1) * (2*N+1)
		mesh = 4*N**2 + 3*N + 1

		#generate J vector (all 0)
		J = ""
		for i in range(mesh):
			J = J + str(0) + " "

		#omit last space (formatting of the read file method)
		file.write(J[:-1] + "\n")


		#generate R vector (all R)
		R = ""
		for i in range(mesh):
			R = R + str(res) + " "

		file.write(R[:-1] + "\n")


		#generate E vector (all 0 except for main branch where we insert a 1V test voltage)
		E = "1 "
		for i in range(mesh - 1):
			E = E + str(0) + " "

		file.write(E[:-1] + "\n")


		file.write("\n")


		#generate the incidence matrix A 
		for i in range(node - 1):
			sub = ""
			for j in range(mesh):
				row = i%(N+1)
				column = i // (N+1)
				node_column = column * (2*N +1) + N + row + 1
				node_row = column*(2*N+1) + row + 1

				
				#test voltage input branch
				if(j == 0 and i == 0): 
					sub = sub + str(-1) + " "

				#check edge cases
				#outwards horizontal branch
				elif(j == (column * (2*N +1) + N + row + 1) and column < 2*N): 
					sub = sub + str(1) + " "

				#outwards vertical branch
				elif(j == (column*(2*N+1) + row + 1) and row < N):
					sub = sub + str(1) + " "

				#inwards horizontal branch
				elif(j == ((column-1) * (2*N +1) + N + row + 1) and column > 0): 
					sub = sub + str(-1) + " "

				#inwards vertical branch
				elif(j == (column*(2*N+1) + row) and row > 0):
					sub = sub + str(-1) + " "

				else:  
					sub = sub + str(0) + " "

			file.write(sub[:-1] + "\n")


