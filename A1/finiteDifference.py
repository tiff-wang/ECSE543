from __future__ import division

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
	def solveBySOR(self, grid, w, threshold, topSymmetry, bottomSymmetry, leftSymmetry, rightSymmetry):
		counter = 0
		underThreshold = False
		while(not underThreshold):
			underThreshold = True
			for i in range(1, len(grid) - 1):
				for j in range(1, len(grid[i]) - 1):
					#check for symmetry conditions: 
					newPotential = (1-w)*grid[i][j] + w/4*(grid[i-1][j] + grid[i][j-1] + grid[i][j+1] + grid[i+1][j])

					#check residual at each node (aka newPotential - oldPotential)
					underThreshold = underThreshold and (newPotential - grid[i][j] < threshold)

					grid[i][j] = newPotential

					if (i == 2 and topSymmetry): grid[0][j] = newPotential
					if (i == len(grid) - 2 and bottomSymmetry): grid[i+1][j] = grid[i-1][j]
					if (j == 2 and leftSymmetry) : grid[i][0] = newPotential
					if (j == len(grid[i]) - 2 and rightSymmetry): grid[i][j+1] = grid[i][j-1]

			counter += 1
			print "\nSOR k = {0}".format(counter)
			for row in grid: print row

