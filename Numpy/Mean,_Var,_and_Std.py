import numpy

a = map(int, raw_input().split())
b = numpy.array([raw_input().split() for i in range(a[0])], int)
print numpy.mean(b, axis = 1)
print numpy.var(b, axis = 0)
print numpy.std(b, axis = None)
