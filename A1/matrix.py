
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

	#method multiplies the matrix * vector and returns de resulting vector
	def matrixVectorMultiplication(self, matrix, vector):
		result = []
		row_size = len(matrix)
		column_size = len(vector)
		for i in range(row_size):
			sum = 0
			for j in range(column_size):
				sum += matrix[i][j] * vector[j]
			result.append(sum)

		return result


	#assuming that the matrix1 and matrix2 are (axn) * (n*b)
	#method multiplies the matrix * vector and returns de resulting vector
	def matrixMultiplication(self, matrix1, matrix2):
		result = []
		row_size = len(matrix1)
		column_size = len(matrix2[0])
		for i in range(row_size):
			row= []
			for j in range(column_size):
				sum = 0
				for k in range(len(matrix2)):
					sum += matrix1[i][k] * matrix2[k][j]
				row.append(sum)
			result.append(row)

		return result

	#compares two vectors, return true if the error between the entries is less than 0.01
	def vectorComparator(self, vector1, vector2):
		for i in range(len(vector1)):
			if math.fabs(vector1[i]-vector2[i]) > 0.01 : return False

		return True


	#takes matrix as input and outputs the transpose 
	def matrixTranspose(self, matrix):
		row_size = len(matrix)
		column_size = len(matrix[0])
		transpose = []
		for i in range(column_size):
			row = []
			for j in range(row_size):
				row.append(matrix[j][i])

			transpose.append(row)

		return transpose

	#method outputs result = vector1 - vector2 (assuming they are of the same length)
	def vectorSubtraction(self, vector1, vector2):
		res = []
		for i in range(len(vector2)):
			res.append(vector1[i]- vector2[i])

		return res


	#method manipulating sparse matrices (assuming properties of incidence matrix of q2)
	#let off1 and b1 be the horizontal offset and bandwidth of Matrix1 respectively
	#let off2 and b2 be the vertical offset and bandwidth of Matrix2 respectively
	#the offset is with respect to the diagonal (if set to null, means that matrix is not banded)

	def sparseMatrixMultiplication(self, matrix1, off1, b1, matrix2, off2, b2):
		result = []
		row_size = len(matrix1)
		column_size = len(matrix2[0])

		for i in range(row_size):
			offset_row = i + off1 if off1 != None else 0
			row= []
			for j in range(column_size):
				sum = 0
				offset_column = j + off2 if off2 != None else 0
				for k in range(max(offset_column, offset_row, 0), 
					min(offset_column+b2, offset_row + b1, len(matrix2))):
					sum += matrix1[i][k] * matrix2[k][j]
				row.append(sum)
			result.append(row)

		return result

	#method manipulating sparse matrices * vector(assuming properties of incidence matrix of q2)
	#let off and b be the horizontal offset and bandwidth of the matrix respectively
	#assume that vector is not sparse
	#the offset is with respect to the diagonal (if set to null, means that matrix is not banded)

	def sparseMatrixVectorMultiplication(self, matrix, off, b, vector):
		result = []
		row_size = len(matrix)
		column_size = len(vector)
		for i in range(row_size):
			offset_row = i + off if off != None else 0
			sum = 0
			for j in range(offset_row, offset_row + b):
				sum += matrix[i][j] * vector[j]
			result.append(sum)

		return result

	#decomposes the banded matrix A into a lower matrix such that L*L^T = A 
	#matrix A altered after the method (replaced by lower matrix L)
	def sparseCholeskiDecomposition(self, matrix, b):
		size = len(matrix)
		for j in range(size): 
			sum = 0
			for i in range(j):
				sum += matrix[j][i] * matrix[j][i]
			matrix[j][j] = math.sqrt(matrix[j][j] - sum)
			
			#fill uper triangle with 0
			for i in range(j):
				matrix[i][j] = 0;
			

			for i in range(j+1, min(j+b, size)):
				sum = 0
				for k in range(max(j - b, 0),j):
					sum += matrix[i][k] * matrix[j][k]
				matrix[i][j] = (matrix[i][j] - sum) / matrix[j][j]

			for i in range(j+b, size):
				matrix[i][j] = 0;

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

	#method solves sparse L * y = vector, returns y 
	def sparseSolvingLowerMatrix(self, matrix, vector, b):
		result = []
		size = len(vector)
		for i in range(size):
			sum = 0
			for j in range(i-b if i - b > 0 else 0, i):
				sum += result[j] * matrix[i][j]
			result.append((vector[i] - sum) / matrix[i][i])
		return result

	#method solves sparse L^T * x = vector, returns x 
	def sparseSolvingTransposeLowerMatrix(self, matrix, vector, b):
		result = []
		size = len(vector)
		for i in range(size)[::-1]: 
			sum = 0
			for j in range(size)[i + b -1 if i + b -1 < size else size:i:-1]:
				sum += result[size-j-1] * matrix[j][i]
			result.append((vector[i] - sum) / matrix[i][i])
		return result[::-1]


	#method solves banded A * x = b using choleski decomposition, returns x
	#method clones input matrix, so the input matrix does not change during the process
	def sparseCholeski(self, matrix, vector, b):
		matrix_clone = copy.deepcopy(matrix)
		self.sparseCholeskiDecomposition(matrix_clone, b)
		y = self.sparseSolvingLowerMatrix(matrix_clone, vector, b)
	 	result = self.sparseSolvingTransposeLowerMatrix(matrix_clone, y, b)
	 	return result
