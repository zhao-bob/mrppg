import pylab as pl

a = pl.arange(0, 2*pl.pi, 0.1)
b = pl.cos(a)
pl.scatter(a, b)
pl.show()
