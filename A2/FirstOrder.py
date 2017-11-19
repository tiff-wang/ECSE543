from matrix import Matrix
from circuit import Circuit

m = Matrix()
c = Circuit()

class FirstOrder(object):
	def __init__(self):
		pass

	def Slocal(self, coord):
		Area = 1.0/2.0 * abs((coord[1][1]-coord[0][1])*(coord[2][0]-coord[0][0]) - 
			(coord[1][0]-coord[0][0])*(coord[2][1]-coord[0][1]))
		S = []
		for i in range(3):
			Si = []
			for j in range(3): 
				y = (coord[(i+1) % 3][1] - coord[(i+2) % 3][1])*(coord[(j+1) % 3][1] - coord[(j+2) % 3][1])
				x = (coord[(i+2) % 3][0] - coord[(i+1) % 3][0])*(coord[(j+2) % 3][0] - coord[(j+1) % 3][0])
				Sij = 1.0 / 4.0 / Area * (y + x)
				Si.append(Sij)
			S.append(Si) 

		return S

	def Sdis(self, triangles):
		S = [[0 for i in range(len(triangles) * 3)] for i in range(len(triangles) * 3)]
		for i in range(len(triangles)):
			local = self.Slocal(triangles[i])
			for j in range(3):
				for k in range(3):
					S[3 * i + j][3 * i + k] = local[j][k]
		return S


	def Sglobal(self, Sdis, C):
		CT = m.matrixTranspose(C);
		SdisC = m.matrixMultiplication(Sdis, C)
		return m.matrixMultiplication(CT, SdisC)

	def Energy(self, S, Ucon):
		SUcon = m.matrixVectorMultiplication(S, Ucon)
		E2 = m.vectorMultiplication(Ucon, SUcon)
		return E2 * 0.5

	def capacitance(self, energy):
		return 2 * energy / 15 / 15 * 8.85 * pow(10, -12)





