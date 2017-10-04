from __future__ import division
from matrix import Matrix
from fileReader import FileReader


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



