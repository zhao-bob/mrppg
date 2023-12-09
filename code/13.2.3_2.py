import numpy as np
from scipy import signal, misc
import matplotlib.pyplot as plt

image = misc.face()
image = np.uint8(image.mean(axis=2))
w = signal.gaussian(50, 10).astype(np.float32)
image_new = signal.sepfir2d(image, w, w)

plt.imshow(image_new)
plt.show()
