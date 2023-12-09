import pylab as pl

x = pl.random(100)
y = pl.random(100)
pl.scatter(x, y, s=x*500, c='r', marker='*')
pl.show()
