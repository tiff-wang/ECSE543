import copy 
from matrix import Matrix

'''
write the format convention of the file

'''


class FileReader(object):
	@staticmethod
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


