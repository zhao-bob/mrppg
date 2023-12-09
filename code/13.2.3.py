import numpy as np
from scipy import signal, misc
import matplotlib.pyplot as plt

image = misc.face()
image = np.uint8(image.mean(axis=2))
w = np.zeros((50,50))
w[0,0] = 1.0
w[49,25] = 1.0
image_new = signal.fftconvolve(image, w)

plt.imshow(image_new)
plt.show()
