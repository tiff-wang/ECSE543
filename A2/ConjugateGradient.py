from matrix import Matrix
import copy, math

m = Matrix()

class ConjugateGradient(object):
	def __init__(self):
		pass

	def matrixGenerator(self):
		A = [[0 for i in range(19)] for j in range(19)]
		for i in range(19):
			if i < 10: 
				if(i < 8): A[i][i+5] = 1
				if i%5 != 0: A[i][i-1] = 1
				if (i+1)% 5 == 0: A[i][i-1] += 1
				else: A[i][i+1] = 1
				if i > 4: A[i][i-5] = 1

			elif i < 13:
				A[i][i-5] = 1
				A[i][i+3] = 1
				if i != 10: A[i][i-1] = 1
				if i != 12: A[i][i+1] = 1

			else:
				A[i][i-3] = 1
				if i < 16: A[i][i+3] = 1
				else: A[i][i-3] += 1
				if i%3 != 0: A[i][i+1] = 1
				if i%3 != 1: A[i][i-1] = 1
			A[i][i] = -4
		return A

	def bGenerator(self):
		b = []
		list = [8, 9, 12, 15, 18]
		for i in range(19):
			if i in list: b.append(-15)
			else: b.append(0)
		return b

	#return answer to Ax = b using Conjugate gradient method
	def ConjugateGradient(self, A, b, residual):
		norm2 = []
		infinity_norm = []
		x = [0 for i in range(len(b))]
		r = self.residue(A, x, b)
		p = copy.deepcopy(r)
		residue = 1
		while(residue < len(A)):
			alpha = self.alpha(A, r, p)
			x = self.newGuess(x, alpha, p)
			r = self.residue(A, x, b)
			beta = self.beta(A, r, p)
			p = self.newOrientation(r, beta, p)
			maxRes = 0
			norm = 0
			for res in r: 
				res = abs(res)
				residue += res
				norm += res*res
				if abs(res) > maxRes : maxRes = res
			residue = math.sqrt(norm)
			norm2.append(math.sqrt(norm))
			infinity_norm.append(maxRes)
		return (x, norm2, infinity_norm)


	
	#pTr/pTAp
	def alpha(self, A, r, p):
		pTr = m.vectorMultiplication(p, r)
		pTA = m.vectorMatrixMultiplication(p, A)
		pTAp = m.vectorMultiplication(pTA, p)
		return float(pTr) / float(pTAp)

	def residue(self, A, x, b):
		Ax = m.matrixVectorMultiplication(A, x)
		return m.vectorDifference(b, Ax)

	def newGuess(self, x, alpha, p):
		alphap = [alpha * i for i in p]
		return m.vectorAddition(x, alphap)

	#-pTAr/pTAp
	def beta(self, A, r, p):
		Ar = m.matrixVectorMultiplication(A, r)
		pTAr = m.vectorMultiplication(p, Ar)
		Ap = m.matrixVectorMultiplication(A, p)
		pTAp = m.vectorMultiplication(p, Ap)
		return -1 * float(pTAr)/float(pTAp)

	#newR + bp
	def newOrientation(self, r, beta, p):
		bp = m.scaleVector(beta, p)
		return m.vectorAddition(r, bp)











