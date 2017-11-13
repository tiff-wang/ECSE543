class FirstOrder(object):
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



fe = FirstOrder()
for row in fe.matrixGenerator(): print row
