from __future__ import division
from matrix import Matrix
import math, copy 

m = Matrix()

# matrix_2x2 = [[9, 24], [24, 73]]
# matrix_3x3 = [[36, 24, -30], [24, 25, -14], [-30, -14, 30]]
# matrix_4x4 = [[1, 4, 2, 9], [4, 25, 11, 36], [2, 11, 86, 36], [9, 36, 36, 254]]
matrix_5x5 = [5,0,0,1,0],[0,5,1,1,3],[0,1,2,0,2],[1,1,0,3,1],[0,3,2,1,8]

# print "\nmatrix 2x2: "
# for row in matrix_2x2: print (row)

# print "\nmatrix 3x3: "
# for row in matrix_3x3: print (row)

# print "\nmatrix 4x4: "
# for row in matrix_4x4: print (row)

print "\nmatrix 5x5: "
for row in matrix_5x5: print (row)

print "\n"

# x2 = [1, 2]
# x3 = [1, 2, 3]
# x4 = [1, 2, 3, 4]
x5 = [1, 2, 3, 4, 5]


# b2 = m.matrixMultiplication(matrix_2x2, x2)
# b3 = m.matrixMultiplication(matrix_3x3, x3)
# b4 = m.matrixMultiplication(matrix_4x4, x4)
# b5 = m.matrixMultiplication(matrix_5x5, x5)
b5 = [29,65,27,32,93]

# print "\nmatrix 2x2 * x2 = {0}".format(b2)
# print "\nmatrix 3x3 * x3 = {0}".format(b3)
# print "\nmatrix 4x4 * x4 = {0}".format(b4)
# print "\nmatrix 5x5 * x5 = {0}".format(b5)


# choleski_sln2 = m.choleski(matrix_2x2, b2)
# choleski_sln3 = m.choleski(matrix_3x3, b3)
# choleski_sln4 = m.choleski(matrix_4x4, b4)
choleski_sln5 = m.choleski(matrix_5x5, b5)
test = m.matrixMultiplication(matrix_5x5, choleski_sln5)
# print ("A*x = {0}".format(test))

# print "x4: {0}".format(x4)
# print "choleski_sln4: {0}".format(choleski_sln4)
# print "choleski_sln5: {0}".format(choleski_sln5)



# print "choleski solution checked for matrix 2: {0}".format(m.vectorComparator(choleski_sln2, x2))
# print "choleski solution checked for matrix 3: {0}".format(m.vectorComparator(choleski_sln3, x3))
# print "choleski solution checked for matrix 4: {0}".format(m.vectorComparator(choleski_sln4, x4))
# print "choleski solution checked for matrix 5: {0}".format(m.vectorComparator(choleski_sln5, x5))

print "choleski solution found: {0}".format(choleski_sln5)
print "choleski solution checked for matrix 5: {0}".format(m.vectorComparator(test, b5))

# m.choleskiDecomposition(matrix_5x5)





