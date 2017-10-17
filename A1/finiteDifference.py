from __future__ import division
import copy

'''
format used in this class: 
	Boundaries conditions: outer square: 0V
							inner square: 15V
	
	Only solve a corner of the map, and use symmetry to 
	find the values to the rest of the voltages 

	The nodes will be stored in a 2D array (list) for easier manipulation
'''

class FiniteDifference(object):
	def __init__(self): 
		pass


	#given a grid of nodes, solve by SOR 
	#assumes the grid is already formatted to be limited to unknown nodes
	#and the boundaries are defined (determine whether the sides are symmetric)
	def solveBySOR(self, grid, w, threshold, topSymmetry, bottomSymmetry, leftSymmetry, rightSymmetry, corner, x, y):
		#if corner == True, then i and j will map the corner of the studied space that have fixed voltage 
		# negative x,y : fixed V > |x|, |y|, positive x, y : fixed V < |x|, |y|
		counter = 0

		underThreshold = False
		while(not underThreshold):
			underThreshold = True
			for i in range(1, len(grid) - 1):
				for j in range(1, len(grid[i]) - 1):
					if(not corner or (corner and not(i < x and j > len(grid[0]) - y -1))):
						# print "i, j: {0}, {1}".format(i, j)
						#check for symmetry conditions: 
						newPotential = (1-w)*grid[i][j] + w/4*(grid[i-1][j] + grid[i][j-1] + grid[i][j+1] + grid[i+1][j])
						# if(i == 1 and j == 1 or j == 2): print newPotential
						#check residual at each node (aka newPotential - oldPotential)
	
						# underThreshold = underThreshold and (newPotential - grid[i][j] < threshold)
						grid[i][j] = newPotential
						if (i == 2 and topSymmetry and (not corner or (corner and j < y))): grid[0][j] = newPotential
						if (i == len(grid) - 2 and bottomSymmetry): grid[i+1][j] = grid[i-1][j]
						if (j == 2 and leftSymmetry) : grid[i][0] = newPotential
						if (j == len(grid[i]) - 2 and rightSymmetry and (not corner or (corner and i >= x))): grid[i][j+1] = grid[i][j-1]

			for i in range(1, len(grid) - 1):
				for j in range(1, len(grid) -1 ):
					residual = grid[i-1][j] + grid[i][j-1] + grid[i][j+1] + grid[i+1][j] - 4*grid[i][j]
					underThreshold = underThreshold and (residual < threshold)

			counter += 1
			# if counter == 1:
			# 	print "\nSOR k = {0}".format(counter)
			# 	for row in grid: print [round(element, 2) for element in row]
			

			# if counter == 100: break
		return counter;

	#map the whole grid after symmetry
	#if Symmetry true, take into account the "false" boundaries inserted in calculations (not to be reflected)
	def mapGrid(self, grid, topSymmetry, bottomSymmetry, leftSymmetry, rightSymmetry):
		if topSymmetry: 
			grid.pop(0)
			for row in grid[0:]:
				grid.insert(0, copy.deepcopy(row))


		if bottomSymmetry: 
			grid.pop(-1)
			for row in grid[-1::-1]:
				grid.append(copy.deepcopy(row))


		if leftSymmetry: 
			for row in grid:
				row.pop(0)
				for element in row[0:]:
					row.insert(0, element)


		if rightSymmetry: 
			for row in grid:
				row.pop(-1)
				for element in row[-1::-1]:
					row.append(element)


	def solveByJacobi(self, grid, threshold, topSymmetry, bottomSymmetry, leftSymmetry, rightSymmetry, corner, x, y):
		#if corner == True, then i and j will map the corner of the studied space that have fixed voltage 
		# negative x,y : fixed V > |x|, |y|, positive x, y : fixed V < |x|, |y|
		counter = 0

		underThreshold = False
		while(not underThreshold):
			underThreshold = True
			tempRow = copy.deepcopy(grid[0])
			for i in range(1, len(grid) - 1):
				tempJ = grid[i][0]
				for j in range(1, len(grid[i]) - 1):
					if(not corner or (corner and not(i < x and j > len(grid[0]) - y -1))):
						#check for symmetry conditions: 
						newPotential = (tempRow[j] + tempJ + grid[i][j+1] + grid[i+1][j])/4
						tempRow[j] = grid[i][j]
						tempJ = grid[i][j]
						grid[i][j] = newPotential
						if (i == 2 and topSymmetry and (not corner or (corner and j < y))): grid[0][j] = newPotential
						if (i == len(grid) - 2 and bottomSymmetry): grid[i+1][j] = grid[i-1][j]
						if (j == 2 and leftSymmetry) : grid[i][0] = newPotential
						if (j == len(grid[i]) - 2 and rightSymmetry and (not corner or (corner and i >= x))): grid[i][j+1] = grid[i][j-1]
					
					else: tempRow[j] = grid[i][j]

			#check residual at each node (aka newPotential - oldPotential)
			for i in range(1, len(grid) - 1):
				for j in range(1, len(grid) -1 ):
					residual = grid[i-1][j] + grid[i][j-1] + grid[i][j+1] + grid[i+1][j] - 4*grid[i][j]
					underThreshold = underThreshold and (residual < threshold)
					
			# print "\nJacobi k = {0}".format(counter)
			# for row in grid: print row
			counter += 1

		return counter;


	#assume this grid generator is taylored to the problem with the described parameteres
	def gridGenerator(self, h):
		size = 0.1 / h + 1; #+1 cause of the symmetry
		grid = [[0 for x in range(int(size))] for y in range(int(size))]
		for i in range(0, int(0.02 / h) + 1):
			for j in range(int(0.06 / h), int(size)): 
				grid[i][j] = 15

		return grid




