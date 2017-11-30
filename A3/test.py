#Tiffany Wang 260684152
#Numerical Methods ECSE 543 - Assignment 3

from curvefitting import CurveFitting
from nonlinear import NonLinear 

cv = CurveFitting() 
nl = NonLinear()


#Question 1

#a)
# B_1 = [0.0, 0.2, 0.4, 0.6, 0.8, 1.0]
# H_1 = [0.0, 14.7, 36.5, 71.7, 121.4, 197.4]

# #get H value at every 0.01
# x = [0.01 * i for i in range(101)]
# result = []
# for i in range(len(x)):
# 	result.append(cv.lagrange(x[i], B_1, H_1))

# file = open("magnetic1.csv", "w")
# for i in range(len(x)):
# 	string = str(x[i]) + ", " + str(result[i]) + "\n"
# 	file.write(string)


#b) 
# B_2 = [0.0, 1.3, 1.4, 1.7, 1.8, 1.9]
# H_2 = [0.0, 540.6, 1062.8, 8687.4, 13924.3, 22650.2]

# #get H value at every 0.01
# x = [0.02 * i for i in range(101)]
# result = []
# for i in range(len(x)):
# 	result.append(cv.lagrange(x[i], B_2, H_2))

# file = open("magnetic2.csv", "w")
# for i in range(len(x)):
# 	string = str(x[i]) + ", " + str(result[i]) + "\n"
# 	file.write(string)

#c) 
# a = [3, 12]
# b = [5, 6]
# print cv.lagrangeDerivativeGenerator(a, 1)
# print cv.lagrangeDerivativeGenerator(a, 3)
# print cv.lagrangeDerivativeGenerator(a, 2)

# print cv.hermiteSub(3.5, a, b, 1)
# B_3 = [0.0, 1.3, 1.4, 1.7, 1.8, 1.9]
# H_3 = [0.0, 540.6, 1062.8, 8687.4, 13924.3, 22650.2]

#get H value at every 0.01
# x = [0.02 * i for i in range(101)]
# result = []
# n = 1;
# for i in range(len(x)):
# 	if (x[i] > B_3[n] and n < len(B_3) - 1): 
# 		n += 1
# 	result.append(cv.hermiteSub(x[i], B_3, H_3, n))

# file = open("magnetic3.csv", "w")
# for i in range(len(x)):
# 	string = str(x[i]) + ", " + str(result[i]) + "\n"
# 	file.write(string)

#Question 2
# result = nl.newtonRaphson(0.0, 1e-6)
# flux = result[0]
# count = result[1]

# print "Approximated flux in the steel core is: ", round(flux, 9), " Wb"
# print "Iteration count: ", count

result = nl.sucSub(0.0000009, 1e-6)
print round(result, 9)




