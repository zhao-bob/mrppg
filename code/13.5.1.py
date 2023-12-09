import pylab as pl

t = pl.arange(0, 2*pl.pi, 0.01)
s = pl.sin(t)
pl.plot(t, s)
pl.xlabel('x')
pl.ylabel('y')
pl.title('sin')
pl.show()
