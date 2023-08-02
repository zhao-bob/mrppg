import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1, 1000000)

hx = np.piecewise(x, [np.log2(np.log2(x)).astype(int) % 2 == 1,  np.log2(np.log2(x)).astype(int) % 2 == 0], [1, 0])

plt.plot(x, np.cumsum(hx)/x)
plt.show()

