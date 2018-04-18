import numpy as np
import matplotlib.pyplot as plt

N1 = 30 
N2 = 135
h1 = 1./N1
h2 = 1./N2

x1 = np.arange(0,1,h1)
x2 = np.arange(0,1,h2)

y1 = np.zeros(N1)
y2 = np.zeros(N2)

y1[0] = 1
y2[0] = 1

def f(x):
    return np.arctan(x)

for i in range(N1-1):
    y1[i+1] = y1[i] + h1*( f(y1[i]) )

for i in range(N2-1):
    y2[i+1] = y2[i] + h2*( f(y2[i]) )

plt.plot(x1, y1, 'r.', linewidth=1)
plt.plot(x2, y2, 'bo')
plt.grid()
plt.show()


