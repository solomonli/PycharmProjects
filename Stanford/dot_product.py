import numpy as np

import time

a = np.random.rand(1000000)
b = np.random.rand(1000000)

tic = time.time()

c = np.dot(a, b)

toc = time.time()

print(c)
print(str(1000 * (toc - tic)) + ' ms')

# np.linalg.norm()
