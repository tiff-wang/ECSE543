from __future__ import division
from matrix import Matrix
import re



class Circuit(object): 
	def __init__(self):
		pass

	def parseElementFile(self, filename):
		file = open(filename, "r")
		element = file.readlines()
		coord = []
		triangles = []
		fixedPotential = []
		C = []

		i = 0
		for line in element:
			temp = line.split("\n")[0].split("\t")
			if len(line) == 1: 
				i+=1
			elif i == 0:
				coord.append(map(float, (temp[1], temp[2])))
			elif i == 1:
				temp = map(int, temp[0].split(" "))
				triangles.append((coord[temp[0] - 1], coord[temp[1] - 1], coord[temp[2] - 1]))
				for count in range(3):
					tempC = [0 for j in range(len(coord))]
					tempC[temp[count] - 1] = 1
					C.append(tempC)
			else:
				fixedPotential.append(map(float, temp));

		return triangles, C

	def parseResultFile(self, filename):
		file = open(filename, "r")
		result = file.readlines();
		U = []
		for row in result: 
			U.append(float(row.split("\n")[0].split(" ")[-1]))
		return U


