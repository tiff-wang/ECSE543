class CurveFitting(object):
	def __init__(self): 
		pass

	#interpolate function using lagrange polynomials (whole domain)
	def lagrange(self, pos, x, y):
		result = 0
		for i in range(len(x)):
			result += y[i] * self.lagrangePolyWhole(pos, x, i)

		return result



	#generate lagrange polynomial coefficients given a set of coordinates of degree index (whole domain)
	def lagrangePolyWhole(self, pos, x, index):
		#the polynomials start counting at 1 (not 0)
		numerator = 1.0
		denominator = 1.0
		for i in range(len(x)):
			if(index != i):
				numerator *= (pos - x[i])
				denominator *= (x[index] - x[i])
		return numerator / denominator



	#generate lagrange polynomial coefficients given a set of coordinates of degree index (subdomain)
	def lagrangePolySub(self, pos, x, n1, n2):
		numerator = float((pos - x[n2]))
		denominator = float(x[n1] - x[n2])
		return numerator / denominator



	#generate dL/dx at degree n 
	def lagrangeDerivativeGenerator(self, x, n1, n2):
		return 1.0 / (x[n1] - x[n2])



	#generate Hermite's U polynomial (subdomain)
	#U_1 ==> (1, 2) 
	#U_2 ==> (2, 1)
	def hermiteU(self, pos, x, n1, n2):
		L = self.lagrangePolySub(pos, x, n1, n2)
		DL = self.lagrangeDerivativeGenerator(x, n1, n2)
		return (1 - 2 * DL * (pos - x[n1])) * L**2



	#generate Hermite's V polynomial (subdomain) 
	#V_1 ==> (1, 2) 
	#V_2 ==> (2, 1)
	def hermiteV(self, pos, x, n1, n2):
		L = self.lagrangePolySub(pos, x, n1, n2)
		return (pos - x[n1]) * L**2


	#approximate result at x in subdomain n 
	def hermiteSub(self, pos, x, y, n):
		result = 0
		b = (y[n] - y[n-1])/(x[n] - x[n-1])

		#j=n-1
		U = self.hermiteU(pos, x, n - 1, n)
		V = self.hermiteV(pos, x, n - 1, n)
		a = y[n - 1]
		result += a * U + b * V


		#j=n
		U = self.hermiteU(pos, x, n, n-1)
		V = self.hermiteV(pos, x, n, n-1)
		a = y[n]
		result += a * U + b * V

		return result






		