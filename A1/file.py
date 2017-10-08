import copy 

'''
The format of the circuit file is assumed to be of the following form: 

#vector J separated with spaces
#vector R separated with spaces
#vector E separated with spaces 
#skip line
#matrix A separated with spaces

example: 
0 0 0 0 0 0
20 10 10 30 30 30
10 0 0 0 0 0

-1 1 1 0 0 0
0 -1 0 1 1 0
0 0 -1 -1 0 1

'''


class File(object):
	@staticmethod
	#function reads J, R, E vectors and A incident matrix from the circuit file 
	#and parse it into a tuple to be further manipulated to find the node voltages
	def parseCircui(filename):
		file = open(filename, "r")
		circuitFile = file.readlines()

		J = map(float, circuitFile[0].split("\n")[0].split(" "))
		R = map(float, circuitFile[1].split("\n")[0].split(" "))
		E = map(float, circuitFile[2].split("\n")[0].split(" "))

		A = []
		for line in circuitFile[4:]:
			A.append(map(float, line.split("\n")[0].split(" ")))


		# print "J: {0}".format(J)
		# print "R: {0}".format(R)
		# print "E: {0}".format(E)
		# print "A: {0}".format(A)

		return (J, R, E, A)


	#function open file
	#and generates the incidence matrix according to the definite difference method. 
	#if file already exists, the current content is erased to be replaced with new incident matrix
	
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




	@staticmethod
	def FDMatrixGenerator(N, res):
		file = open("finite-diff-matrix.txt", 'w')
		
		node = (N+1) * (2*N+1)
		mesh = 4*N**2 + 3*N + 1

		#generate J vector (all 0)
		J = ""
		for i in range(mesh):
			J = J + str(0) + " "

		#omit last space (formatting of the read file method)
		#TODO change to write into the file later + new line
		print (J[:-1])


		#generate R vector (all R)
		R = ""
		for i in range(mesh):
			R = R + str(res) + " "

		print (R[:-1])

		#generate E vector (all 0 except for main branch where we insert a 1V test voltage)
		V = "1 "
		for i in range(mesh - 1):
			V = V + str(0) + " "

		print (V[:-1])

		print "" 


		#generate the incidence matrix A 
		for i in range(node - 1):
			sub = ""
			for j in range(mesh):
				row = i%(N+1)
				column = i // (N+1)
				node_column = column * (2*N +1) + N + row + 1
				node_row = column*(2*N+1) + row + 1
				# print "node_column: {0}".format(node_column)
				# print "node_row: {0}".format(node_row)
				
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

			print (sub[:-1])

		
        #j = column number (0 .. 2N)
        #i = row number (0 .. N)
		#vertical mesh number = j(2N + 1) + j + 1
		#horizontal mesh number = j(2N + 1 ) N + i + 1






