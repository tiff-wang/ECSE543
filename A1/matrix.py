
from __future__ import division
import math, copy

# import pdb

class Matrix(object):
	def __init__(self): 
		pass


	#decomposes the matrix A into a lower matrix such that L*L^T = A 
	#matrix A altered after the method (replaced by lower matrix L)
	def choleskiDecomposition(self, matrix):
		size = len(matrix)
		for j in range(size): 
			sum = 0
			for i in range(j):
				sum += matrix[j][i] * matrix[j][i]
			matrix[j][j] = math.sqrt(matrix[j][j] - sum)
			for i in range(j):
				matrix[i][j] = 0;
			for i in range(j+1, size):
				sum = 0
				for k in range(j):
					sum += matrix[i][k] * matrix[j][k]
				matrix[i][j] = (matrix[i][j] - sum) / matrix[j][j]

		print ("decomposition of matrix: ")
		for row in matrix: print(row)
		print "\n"


	#method executes A*A^T. prints resulting matrix 
	def decompositionCheck(self, matrix):
		LLT = []
		for i in range(len(matrix)):
			LLT.append([])
			for j in range(len(matrix)):
				sum = 0 
				for k in range(len(matrix)):
					sum += matrix[i][k] * matrix[j][k]
				LLT[i].append(sum)
		for row in LLT: 
			print (row)


	#method solves L * y = b, returns y 
	def solvingLowerMatrix(self, matrix, vector):
		result = []
		size = len(vector)
		for i in range(size):
			sum = 0
			for j in range(i):
				sum += result[j] * matrix[i][j]
			result.append((vector[i] - sum) / matrix[i][i])
		return result

	#method solves L^T * x = y, returns x 
	def solvingTransposeLowerMatrix(self, matrix, vector):
		result = []
		size = len(vector)
		for i in range(size)[::-1]: 
			sum = 0
			for j in range(size)[:i:-1]:
				sum += result[size-j-1] * matrix[j][i]
			result.append((vector[i] - sum) / matrix[i][i])
		return result[::-1]


	#method solves A * x = b using choleski decomposition, returns x
	#method clones input matrix, so the input matrix does not change during the process
	def choleski(self, matrix, vector):
		matrix_clone = copy.deepcopy(matrix)
		self.choleskiDecomposition(matrix_clone)
		y = self.solvingLowerMatrix(matrix_clone, vector)
	 	result = self.solvingTransposeLowerMatrix(matrix_clone, y)
	 	return result


	#method checks if matrix * solution = vector
	def checkMatrixSolution(self, matrix, solution, vector):
		for i in range(len(matrix)):
			sum = 0
			for j in range(len(matrix)):
				sum += matrix[i][j] * solution[j]
			if math.fabs(vector[i] - sum) > 0.01:
				return False
		return True

	def matrixMultiplication(self, matrix, vector):
		result = []
		size = len(matrix)
		for i in range(size):
			sum = 0
			for j in range(size):
				sum += matrix[i][j] * vector[j]
			result.append(sum)

		return result

	def vectorComparator(self, vector1, vector2):
		for i in range(len(vector1)):
			if math.fabs(vector1[i]-vector2[i]) > 0.01 : return False

		return True