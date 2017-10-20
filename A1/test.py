from __future__ import division
from matrix import Matrix
from circuit import Circuit
from finiteDifference import FiniteDifference
import math, copy, os, time

m = Matrix()
c = Circuit()
fd = FiniteDifference()

#========================== TEST MATRIX ========================

matrix1 =[[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 1]]
matrix2 =[[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]

vector = [1, 2, 3, 4]

#============================== END ============================



#========================= PART 1 TEST ================================


# import all testCircuit files in a list
testCiruits = []
for file in os.listdir("."):
    if file.startswith("testCircuit"): testCiruits.append(file)


#========================= Choleski Decomposition test Matrices ================================

# matrix_2x2 = [[9, 24], [24, 73]]
# matrix_3x3 = [[36, 24, -30], [24, 25, -14], [-30, -14, 30]]
# matrix_4x4 = [[1, 0, 3, 1], [0, 4, 8, 0], [3, 8, 26, 5], [1, 0 , 5, 30]]
# matrix_5x5 = [5,0,0,1,0],[0,5,1,1,3],[0,1,2,0,2],[1,1,0,3,1],[0,3,2,1,8]
# matrix_5x5 = [[27, 2, 21, 0, 1], [2, 8, 2, 0, 2], [21, 2, 26, 6, 1], [0, 0, 6, 4, 0],[ 1, 2, 1, 0, 1]]


# x2 = [1, 2]
# x3 = [1, 2, 3]
# x4 = [1, 2, 3, 4]
# x5 = [1, 2, 3, 4, 5]

# b2 = m.matrixVectorMultiplication(matrix_2x2, x2)
# b3 = m.matrixVectorMultiplication(matrix_3x3, x3)
# b4 = m.matrixVectorMultiplication(matrix_4x4, x4)
# b5 = m.matrixVectorMultiplication(matrix_5x5, x5)
# b5 = [29,65,27,32,93]




# choleski_sln2 = m.choleski(matrix_2x2, b2)
# choleski_sln3 = m.choleski(matrix_3x3, b3)
# choleski_sln4 = m.choleski(matrix_4x4, b4)
# choleski_sln5 = m.choleski(matrix_5x5, b5)
#================================ END ================================




#=============== MATRIX COMPUTATION RESULT PRINT =============
# print "matrix 2x2: "
# for row in matrix_2x2: print (row)
# print "\nx2 = {0}".format(x2)
# print "matrix 2x2 * x2 = {0}".format(b2)
# print "choleski solution: {0}".format(choleski_sln2)
# print "choleski solution checked for matrix 2: {0}".format(m.vectorComparator(choleski_sln2, x2))



# print "\n\nmatrix 3x3: "
# for row in matrix_3x3: print (row)
# print "\nx3 = {0}".format(x3)
# print "matrix 3x3 * x3 = {0}".format(b3)
# print "choleski solution: {0}".format(choleski_sln3)
# print "choleski solution checked for matrix 3: {0}".format(m.vectorComparator(choleski_sln3, x3))



# print "\n\nmatrix 4x4: "
# for row in matrix_4x4: print (row)
# print "\nx4 = {0}".format(x4)
# print "matrix 4x4 * x4 = {0}".format(b4)
# print "choleski solution: {0}".format(choleski_sln4)
# print "choleski solution checked for matrix 4: {0}".format(m.vectorComparator(choleski_sln4, x4))



# print "\n\nmatrix 5x5: "
# for row in matrix_5x5: print row
# print "\nx5 = {0}\n".format(x5)
# print "matrix 5x5 * x5 = {0}".format(b5)
# print "choleski solution: {0}".format([round(element, 3) for element in choleski_sln5])
# print "choleski solution checked for matrix 5: {0}".format(m.vectorComparator(choleski_sln5, x5))
#================================ END ================================



#========================== TEST MATRIX ========================

#matrix1 =[[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
#matrix2 =[[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]

# print m.matrixMultiplication(matrix1, matrix2)
# print m.matrixTranpose(matrix1)
#============================== END ============================

# print "\n\n"

#========================== TEST CIRCUITS ========================
for file in testCiruits: 
	print "{0}: {1}".format(file, [round(element, 2) for element in c.findNodeVoltage(c.parseCircuit(file))])

# print "{0}: {1}".format("testCircuit4.txt", c.findNodeVoltage(c.parseCircuit(file)))
#============================== END ============================


#========================= PART 1 TEST  END ================================


#========================= PART 2 TEST ================================

# c.FDMatrixGenerator(1, 1000)
# nodeV = c.findNodeVoltage(c.parseCircuit("finite-diff-matrix.txt"))

# print c.findReq(1, 1000)


# find Req for all N = 2 .. 10 and compute runtime for each N 
# for N in range(2, 11):
#  	start = time.clock()
#  	res = c.findReq(N, 1000)
#  	end = time.clock()
#  	runtime = (end - start) * 1000
#  	print "N = {0}:   Req = {1} ohm   Runtime={2} ms".format(N, res, runtime)

# print "" 
# # find Req using sparse matrix properties for all N = 2 .. 10 and compute runtime for each N 
# for N in range(2, 11):
#  	start = time.clock()
#  	res = c.sparsefindReq(N, 1000)
#  	end = time.clock()
#  	runtime = (end - start) * 1000
#  	print "N = {0}:   Req = {1} ohm   Sparse Runtime={2} ms".format(N, res, runtime)





#=========================SPARSEMATRIX TEST ================================
#start = time.time()
#sparseMultiplication = m.sparseMatrixMultiplication(matrix1, matrix2)
#print(time.time() - start) * 1000
#for row in sparseMultiplication:
	# print row

#start = time.time()
#sparseMultiplication = m.matrixMultiplication(matrix1, matrix2)
#print(time.time() - start) * 1000
#for row in sparseMultiplication:
	# print row


# circuitNetwork = c.parseCircuit("q2CircuitFile-2.txt")
# J = circuitNetwork[0]
# R = circuitNetwork[1]
# E = circuitNetwork[2]
# A = circuitNetwork[3]
# Y = [[0 for x in range(len(R))] for y in range(len(R))]
		
# for i in range(len(Y)):
# 	Y[i][i] = 1/R[i]

# print "\nA"
# for row in A: print(row)

# b = len(A[0]) - len(A) + 1


# print "\ntranspose A"
# for row in m.matrixTranspose(A): print (row)

# print "\nYA^T sparse"
# for row in m.sparseMatrixMultiplication(Y, 0, 1, m.matrixTranspose(A), 0, b): print (row)

# print "\nYA^T"
# for row in m.matrixMultiplication(Y, m.matrixTranspose(A)): print (row)

# print "normal" 
# for row in m.matrixMultiplication(A, m.matrixTranspose(A)): print (row)


# print "\nsparse"
# for row in m.sparseMatrixMultiplication(A, 0, b, m.matrixTranspose(A), 0, b): print (row)

# print "\n matrix * vector"
# print m.matrixVectorMultiplication(matrix1, vector)

# print "\n sparse matrix * vector"
# print m.sparseMatrixVectorMultiplication(matrix1, 0, 5, vector)

# print "\nAYA^T"
# AYAT = m.matrixMultiplication(A, m.matrixMultiplication(Y, m.matrixTranspose(A)))
# for row in AYAT: print row

# sparseAYAT = m.sparseMatrixMultiplication(A, 0, b, m.sparseMatrixMultiplication(Y, 0, 1, m.matrixTranspose(A), 0, b), 0, b)
# for row in sparseAYAT: print row


# print "\nlower "
# m.choleskiDecomposition(AYAT)
# for row in AYAT: print row 

# print "\nsparse lower "
# m.sparseCholeskiDecomposition(sparseAYAT, 5)
# for row in sparseAYAT: print row 

# b = m.matrixVectorMultiplication(A, m.vectorSubtraction(J, m.matrixVectorMultiplication(Y, E)))

# vector = m.sparseMatrixVectorMultiplication(A, 0, 4, m.vectorSubtraction(J, m.sparseMatrixVectorMultiplication(Y, 0, 1, E)))

# print "\nvector"
# print b

# print "\nsparseVector"
# print vector

#at this point AYAT is a L matrix
# print "\nsolve Lower"
# print m.solvingLowerMatrix(AYAT, b)

# print "\nsolve SparseLower"
# print m.sparseSolvingLowerMatrix(sparseAYAT, b, 3)

# y = m.solvingLowerMatrix(AYAT, b)
# print "\nsolve LowerTranpose"
# print m.solvingTransposeLowerMatrix(AYAT, y)

# print "\nsolve SparseLowerTranpose"
# print m.sparseSolvingTransposeLowerMatrix(sparseAYAT, y, 3)

# print "\nfindNodeVoltage"
# print c.findNodeVoltage(circuitNetwork)

# print "\nsparsefindNodeVoltage"
# print c.sparseFindNodeVoltage(circuitNetwork, 1)


#=========================SPARSEMATRIX TEST END ================================


#=========================SPARSE CHOLESKI TEST =================================


# print "sparsefindReq"
# print c.sparsefindReq(2,1000)
# print "findReq"
# print c.findReq(2, 1000)

#=========================SPARSE CHOLESKI TEST END ================================



#=========================FINITE DIFFERENCE TEST =================================
# grid = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1]]


#0.1 - 0.04 = 0.06 and 0.1 - 0.02 = 0.08
#h = 0.02 
# grid = [[0, 0, 0, 15, 15, 15], [0, 0, 0, 15, 15, 15], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]


# fd.solveBySOR(grid, 1, 0.00001, True, False, False, True, True, 2, 2)
# gridSOR = copy.deepcopy(grid)
# counter = fd.solveBySOR(gridSOR, 1.4, 0.00001, True, False, False, True, True, 2, 3);
# print "counter: {0}".format(counter)
# for row in gridSOR : print row

# gridJacobi = copy.deepcopy(grid)
# print ""
# for row in gridJacobi: print row

# counter = fd.solveByJacobi(gridJacobi, 0.00001, True, False, False, True, True, 2, 3);
# print "counter: {0}".format(counter)
# for row in gridJacobi: print row
# print ""


# print "\nlower left corner"
# for row in grid: 
# 	rounded = [ round(elem, 2) for elem in row ]
# 	print rounded

# fd.mapGrid(grid, True, False, False, True)
# # fd.mapGrid(gridTest, False, False, False, True)

# print "\nwhole map"
# for row in grid: 
# 	rounded = [ round(elem, 2) for elem in row ]
# 	print rounded



#============== varying w ==================
#w : from 1.0 to 2.0 with step = 0.1
# grid = [[0, 0, 0, 15, 15, 15], [0, 0, 0, 15, 15, 15], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
# for w in range(10, 20):
# 	print "for w = {0}".format(w/10)
# 	gridTest = copy.deepcopy(grid)
# 	counter = fd.solveBySOR(gridTest, w/10, 0.00001, True, False, False, True, True, 2, 2)
# 	fd.mapGrid(gridTest, True, False, False, True)
# 	print "solved in {0} iteration. Potential at (0.06, 0.04): {1}\n".format(counter, gridTest[2][3])



#============== varying h ==================
# h = [0.02, 0.01, 0.005, 0.001]
# h = [0.01]
#SOR
# print "using SOR"
# for step in h:
# 	grid = fd.gridGenerator(step)
# 	fd.solveBySOR(grid, 1.4, 0.00001, True, False, False, True, True, int(0.02/step)+1, int(0.04/step) + 1)

# 	# if(step > 0.005):
# 	# 	for row in grid: print [round(element, 2) for element in row]

# 	print ""

# 	fd.mapGrid(grid, True, False, False, True)
# 	if(step > 0.005):
# 		for row in grid: print [round(element, 2) for element in row]

# 	print "h={0} and w=1.4    Potential at (0.06, 0.04): {1}".format(step, grid[int(0.04/step)][int(0.06/step)])

#Jacobi
# print "\nusing Jacobi"
# for step in h:
# 	grid = fd.gridGenerator(step)
# 	fd.solveByJacobi(grid, 0.00001, True, False, False, True, True, int(0.02/step)+1, int(0.04/step) + 1)
	
# 	fd.mapGrid(grid, True, False, False, True)
# 	# if(step > 0.005):
# 	# 	for row in grid: print row

# 	print "h={0}     Potential at (0.06, 0.04): {1}".format(step, grid[int(0.04/step)][int(0.06/step)])


#=========================FINITE DIFFERENCE TEST END ================================



#=========================NON-UNIFORM NODE SPACING FINITE DIFFERENCE TEST =================================
i_coord = [0, 0.025, 0.035, 0.04, 0.045, 0.05, 0.06, 0.075, 0.09, 0.1, 0.11] #focus on y
j_coord = [0, 0.02, 0.04, 0.05, 0.055, 0.06, 0.065, 0.07, 0.085, 0.1, 0.115] #focus on x

# i_coord = [0.1 * x for x in range(10)] #focus on y
# j_coord = [0.1 * x for x in range(10)] #focus on x

grid = [[0, 0, 0, 0, 0, 15, 15, 15, 15, 15, 15], [0, 0, 0, 0, 0, 15, 15, 15, 15, 15, 15], [0, 0, 0, 0, 0, 15, 15, 15, 15, 15, 15], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]




# grid = [[0, 0, 0, 15, 15, 15], [0, 0, 0, 15, 15, 15], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
grid2 = fd.gridGenerator(0.01)
fd.nonUniformSOR(grid, 1.4, 0.00001, True, False, False, True, True, 3, 7, i_coord, j_coord)
# fd.mapGrid(grid, True, False, False, True)

fd.solveBySOR(grid2, 1.4, 0.00001, True, False, False, True, True, 3, 5)
# fd.mapGrid(grid2, True, False, False, True)

print "non uniform"
for row in grid[1:]: print [round(element, 2) for element in row[:-1]]

print "\nuniform"
for row in grid2[1:]: print [round(element, 2) for element in row[:-1]]





#=========================NON-UNIFORM NODE SPACING FINITE DIFFERENCE TEST END=================================

