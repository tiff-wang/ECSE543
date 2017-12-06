from curvefitting import CurveFitting

B = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9]
H = [0.0, 14.7, 36.5, 71.7, 121.4, 197.4, 256.2, 348.7, 540.6, 1062.8, 2318.0, 4781.8, 8687.4, 13924.3, 22650.2]
A = 0.0001
Rg = 3.978873577e7 
NI = 8000


cv = CurveFitting()

class NonLinear(object):
	def __init__(self):
		pass

	#this newtonRaphson method is for the assignment problem only
	#return approximated flux in the steel core
	def newtonRaphson(self, guess, threshold):
		flux = guess
		count = 0
		H_cur = self.Hcur(flux)
		f_0 = 0.3 * H_cur - NI
		while(abs(self.fcur(flux) / f_0) > 1e-6):
			flux = flux - self.fcur(flux) / self.fder(flux)
			count += 1
		return (flux, count)

	def fder(self, flux):
		return Rg + 0.3 * self.Hder(flux) / A

	def fcur(self, flux):
		# print "hcur: ", self.Hcur(flux)
		return Rg * flux + 0.3 * self.Hcur(flux)- NI

	#consider piecewise linear functions when finding H and H_derivative
	def Hder(self, flux):
		b = flux / A
		if b > B[-1] : 
			return (H[-1] - H[-2]) / (B[-1] - B[-2])

		for i in range(len(B)):
			if(B[i] > b):
				return (H[i] - H[i - 1]) / (B[i] - B[i - 1])

		return (H[1] - H[0]) / (B[1] - B[0])
					

	def Hcur(self, flux):
		b = flux / A
		m = self.Hder(b)
		if b > B[-1] : 
			return H[-1] + (b - B[-1]) * m

		for i in range(len(B)):
			if(B[i] > b):
				return H[i - 1] + (b - B[i - 1]) * m


		return H[0] + (b - B[0]) * m


	def sucSub(self, guess, threshold):
		f_0 = self.fcur(0)
		flux = guess
		count = 0
		while(abs(self.fcur(flux) / f_0) > threshold):
			flux = self.fsub(flux)
		return flux

	def fsub(self, flux):
		return NI / (Rg + 0.3 * self.Hcur(flux)/flux)



# def fSubstitution(flux):
# return 8000/(39.78873577e6 + 0.3 * Hval(flux)/flux)
# def succesSub (x,tolerance):
# i = 0
# while abs(fFlux(x)/fFlux(0)) > tolerance:
# i += 1
# x = fSubstitution(x)
# print('Iterations: ' + str(i) + ' Flux: ' + str(x))
# return x
# NR = newtonRaph(0.0, 1e-6)













