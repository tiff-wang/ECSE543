import copy 
from matrix import Matrix

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


class FileReader(object):
	@staticmethod

	#function reads J, R, E vectors and A incident matrix from the circuit file 
	#and parse it into a tuple to be further manipulated to find the node voltages
	def parseCircuitFile(filename):
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


