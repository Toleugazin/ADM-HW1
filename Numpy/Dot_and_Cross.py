import numpy

N = int(raw_input())
A = numpy.array([raw_input().split() for i in range(N)], int)
B = numpy.array([raw_input().split() for i in range(N)], int)
print numpy.dot(A, B)
