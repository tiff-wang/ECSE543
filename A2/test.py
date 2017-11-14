from FirstOrder import FirstOrder
from circuit import Circuit
from ConjugateGradient import ConjugateGradient
from matrix import Matrix
import copy




fo = FirstOrder()
c = Circuit()
m = Matrix()

#========================================TESTING FILEREADER ================================================
circuit = c.parseElementFile("file.dat")
Ucon =  c.parseResultFile("result.dat")

# for element in circuit: 
# 	for row in element: print row
#========================================END FILEREADER ================================================


#========================================TESTING FIRSTORDER ================================================
triangle = circuit[0]
C = circuit[1]
Slocal =  fo.Slocal(triangle[0])
# print "Slocal:"
# for row in Slocal: print row

# print "\nSdis:"
# Sdis = fo.Sdis(triangle)
# for row in Sdis: print [round(element, 2) for element in row]

# Sglobal = fo.Sglobal(Sdis, C)
# print "\nSglobal:"
# for row in Sglobal: print [round(element, 2) for element in row]

# print "\nC:"
# for row in C: print row
# print len(Sglobal[0])
# print len(Ucon)
# energy = fo.Energy(Sglobal, Ucon)
# print "energy = {0}".format(energy)

# totalEnergy = energy * 4
# cap = 2 * totalEnergy / 15 / 15 * 8.85 * pow(10, -12)
# print "cap = {0}".format(cap) 


#========================================END FIRSTORDER ================================================

#========================================TESTING CONJUDATE GRADIENT ================================================
cg = ConjugateGradient()
A = cg.matrixGenerator()
b = cg.bGenerator()
AT = m.matrixTranspose(A)
ATA = m.matrixMultiplication(AT, A)
ATb = m.matrixVectorMultiplication(AT, b)

# for row in ATA: print row
# print 

# print ATb

# potential = m.choleski(ATA, ATb)
# print [round(element, 2) for element in potential]

#(0.06, 0.04) is node 11
# print "potential at (0.06, 0.04): {0}".format(round(potential[11],2))

# p = [1, 1, 1, 1]
# r = [5, 6, 7, 8]
# A = [[i for i in range(4)] for i in range(4)]

# print cg.rearrange(A, r, p)
answer = cg.ConjugateGradient(A, b, 0.005)
#(0.06, 0.04) is node 11
x = answer[0]
print [round(pot, 2) for pot in x]
norm2 = answer[1]
infinity_norm = answer[2]
print "potential at (0.06, 0.04): {0}".format(round(x[11],2))


for i in range(len(norm2)):
	print "iteration {0}:       2norm: {1}      infinity_norm: {2}".format(i, round(norm2[i], 3), round(infinity_norm[i], 3))




#========================================END CONJUDATE GRADIENT================================================
