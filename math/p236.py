from scipy.special import perm, comb

import numpy as np
import matplotlib.pyplot as plt

r = np.arange(53)
res = []

for k in range(1, 5):
    fr = np.cumsum(perm(4, k) * comb(r - 1, k - 1) * perm(48, r - k) / perm(52, r))
    res.append(np.min(np.where(fr >= 0.5)))
    plt.plot(r, fr)
plt.show()
print(res)
