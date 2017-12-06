#Tiffany Wang 260684152
#Numerical Methods ECSE 543 - Assignment 3

import math
from curvefitting import CurveFitting
from nonlinear import NonLinear 
from circuit import Circuit
from integration import Integration

cv = CurveFitting() 
nl = NonLinear()
c = Circuit()
i = Integration()


#======================================Question 1======================================

# # a)
# B_1 = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
# H_1 = [0.0, 14.7, 36.5, 71.7, 121.4, 197.4]

# #get H value at every 0.01
# x = [0.01 * i for i in range(101)]
# result = []
# for i in range(len(x)):
# 	print "B: ", i, "   H: ", round(cv.lagrange(x[i], B_1, H_1), 5)
# 	result.append(cv.lagrange(x[i], B_1, H_1))


# file = open("magnetic1.csv", "w")
# for i in range(len(x)):
# 	string = str(x[i]) + ", " + str(result[i]) + "\n"
# 	file.write(string)


# #b) 
# B_2 = [0.0, 1.3, 1.4, 1.7, 1.8, 1.9]
# H_2 = [0.0, 540.6, 1062.8, 8687.4, 13924.3, 22650.2]

# get H value at every 0.01
# x = [0.02 * i for i in range(101)]
# result = []
# for i in range(len(x)):
# 	print "B: ", i, "   H: ", round(cv.lagrange(x[i], B_2, H_2))
# 	result.append(cv.lagrange(x[i], B_2, H_2))

# file = open("magnetic2.csv", "w")
# for i in range(len(x)):
# 	string = str(x[i]) + ", " + str(result[i]) + "\n"
# 	file.write(string)

# # c) 
# a = [3, 12]
# b = [5, 6]
# print cv.lagrangeDerivativeGenerator(a, 1)
# print cv.lagrangeDerivativeGenerator(a, 3)
# print cv.lagrangeDerivativeGenerator(a, 2)

# print cv.hermiteSub(3.5, a, b, 1)
# B_3 = [0.0, 1.3, 1.4, 1.7, 1.8, 1.9]
# H_3 = [0.0, 540.6, 1062.8, 8687.4, 13924.3, 22650.2]

# #get H value at every 0.01
# x = [0.02 * i for i in range(101)]
# result = []
# n = 1;
# for i in range(len(x)):
# 	if (x[i] > B_3[n] and n < len(B_3) - 1): 
# 		n += 1
# 	print "B: ", i, "   H: ", round(cv.hermiteSub(x[i], B_3, H_3, n))
# 	result.append(cv.hermiteSub(x[i], B_3, H_3, n))

# file = open("magnetic3.csv", "w")
# for i in range(len(x)):
# 	string = str(x[i]) + ", " + str(result[i]) + "\n"
# 	file.write(string)

#======================================Question 2======================================
result = nl.newtonRaphson(0.0, 1e-6)
flux = result[0]
count = result[1]

print "Approximated flux in the steel core is: ", round(flux, 9), " Wb"
print "Iteration count: ", count

result = nl.sucSub(0.0009, 1e-6)
print round(result, 9)

# print "Approximated flux in the steel core is:  0.00016066  Wb" 

#======================================Question 3======================================

# v = [0, 0]
# result = c.newtonRaphson(v, 5e-10)
# vlog = result[1]
# flog = result[0]

# for row in vlog: print "vn: ", [round(elem, 10) for elem in row]
# for row in flog: print "fn: ", [round(elem, 10) for elem in row]

# for i in range(len(vlog)):
# 	print "iteration ", i, ": ", "VA = ", str(round(vlog[i][1] - vlog[i][0], 4)), "  VB = ", str(round(vlog[i][0], 4))
# 	print "f: ", [round(elem, 6) for elem in flog[i]], "   vn: ", [round(elem, 4) for elem in vlog[i]], "\n"

# matrix =  [[4, 7], [2, 6]]

#======================================Question 4======================================
# the answer of Int(cos(x)) from x = 0 to x = 1 is sin(1)
# answer = math.sin(1)
# file = open("cos.csv", "w")

# # print result and parse it into a csv file for graphing purposes for cos
# for n in range(1, 21):
# 	res = i.GL1P(math.cos, n, 0, 1)
# 	error = abs(answer - res)
# 	print "N = ", n, "  res = ", res, "  error = ", error
# 	file.write(str(math.log10(n)) + ", " + str(math.log10(error)) + "\n")

# print "\n"

# # the answer of Int(log(x)) from x = 0 to x = 1 is x*lnx - x = -1
# answer = -1
# file = open("log.csv", "w")

# #print result and parse it into a csv file for graphing purposes for log
# for m in [(10 * d) for d in range(1, 21)]:
# 	res = i.GL1P(math.log, m, 0, 1)
# 	error = abs(answer - res)
# 	print "N = ", m, " res = ", res, "  error = ", error
# 	file.write(str(math.log(m)) + ", " + str(math.log(error)) + "\n")

# coord = [0.0, 0.025, 0.086, 0.15, 0.28, 0.37, 0.5, 0.640, 0.75, 0.85, 1]


# res = i.Gl1PNonUni(math.log, coord)
# error = abs(answer - res)
# print "Non uniform segments: res = ", res, "  error = ", error




