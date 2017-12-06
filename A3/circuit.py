#q3 non linear circuit 

E = 0.22
R = 500
Isa = 0.6e-6
Isb = 1.2e-6
ktq = 25e-3

import math 
from matrix import Matrix

m = Matrix()


class Circuit(object):
	def __init__(self):
		pass

	def newtonRaphson(self, vn, threshold):
		#f1 = E - RIs(e^(q*V1/kt) - 1) - V2
		flog = []
		vlog = []

		while True:
			v2 = vn[1]
			v1 = vn[0]
			f1 = E - R * Isb * math.expm1(v1 / ktq) - v2
			f2 = Isa*(math.exp((v2 - v1) / ktq) - 1.0) - Isb*math.expm1(v1 / ktq)

			f = [f1, f2]

			J = [[None for x in range(2)] for y in range(2)]
			J[0][0] = f1der1(v1, v2)
			J[0][1] = f1der2(v1, v2)
			J[1][0] = f2der1(v1, v2)
			J[1][1] = f2der2(v1, v2)

			Jinv = inverse(J)

			Jinvf = m.matrixVectorMultiplication(Jinv, f)
			vn = m.vectorDifference(vn, Jinvf)

			flog.append(f)
			vlog.append(vn)

			if abs(f1) < threshold: break

		return (flog, vlog)

def f1der1(v1, v2):
	return - R * Isb * math.exp(v1 / ktq) / ktq

def f1der2(v1, v2):
	return -1.0


def f2der1(v1, v2):
	return - Isa / ktq * math.exp((v2-v1)/ktq) - Isb/ktq * math.exp(v1/ktq)

def f2der2(v1, v2):
	return Isa / ktq * math.exp((v2-v1)/ktq)

def inverse(matrix):
	det = 1.0/(matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1])
	temp = matrix[0][0] 
	matrix[0][0] = matrix[1][1] * det
	matrix[1][1] = temp * det

	matrix[1][0] *= -1.0 * det
	matrix[0][1] *= -1.0 * det

	return matrix