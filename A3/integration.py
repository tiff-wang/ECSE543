class Integration:
	def __init__(self):
		pass

	def GL1P(self, f1, n, s, e):
		n, s, e = float(n), float(s), float(e)
		w = 2 
		x = 0
		n = (e - s) / n
		sum = 0 
		while(s < e):
			e2 = s + n
			sum += (e2 - s)* f1((e2 - s) / 2.0 * x + (s + e2) / 2.0)
			s += n

		return sum

	def Gl1PNonUni(self, f1, coord):
		w = 2 
		x = 0
		sum = 0
		for i in range(1, len(coord)):
			e = coord[i]
			s = coord[i - 1]
			n = e - s
			# print (e - s) * f1((e - s) / 2.0 * x + (s + e) / 2.0)
			sum += (e - s) * f1((e - s) / 2.0 * x + (s + e) / 2.0)

		return sum
