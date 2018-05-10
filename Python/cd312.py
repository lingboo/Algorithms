import numpy as np
import time
def f16(a, b):
    return sum(a[i]*b[i] for i in range(len(a)))
a = np.random(100000)
b = np.random(100000)
begin = time.time()
np.dot(a, b)
end = time.time()
print(1000*(end-begin))

begin = time.time()
f16(a, b)
end = time.time()
print(1000*(end-begin))
