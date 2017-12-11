
import numpy

X = numpy.array([[1,0,0],[1,0,1],[1,1,0],[1,1,1]])
w = numpy.array([0,0,0])
y = numpy.array([1,1,1,0])
h = numpy.array([0,0,0,0])

print("x1\tx2\tw0\tw1\tw2\tsum\toutput\ty")
print("----------------------------------------------------------")
while (h != y).any():
    for i, x in enumerate(X):
        total = x[1] * w[1] + x[2] * w[2] + w[0]
        if total > 0:
            h[i] = 1
        else:
            h[i] = 0
        print("%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d" % (x[1],x[2],w[0],w[1],w[2],total,h[i],y[i]))
        for j in range(3):
            w[j] = w[j] + (y[i] - h[i]) * x[j]

# convergence
print("\nConvergence")
print("x1\tx2\tw0\tw1\tw2\tsum\toutput\ty")
print("----------------------------------------------------------")
for i, x in enumerate(X):
    total = x[1] * w[1] + x[2] * w[2] + w[0]
    if total > 0:
        h[i] = 1
    else:
        h[i] = 0
    print("%d\t%d\t%d\t%d\t%d\t%d\t%d\t%d" % (x[1],x[2],w[0],w[1],w[2],total,h[i],y[i]))

