import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize 


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

def F(Y, h, yk):
    return Y - h*np.arctan(Y) - yk

y0 = 0
# Metodo de Euler Implicito para 30 pontos
for i in range(N1-1):
    y1[i+1] = optimize.newton(F, y1[i], args=(h1, y1[i],))

# Metodo de Euler Implicito para 135 pontos
for i in range(N2-1):
    y2[i+1] = optimize.newton(F, y2[i], args=(h2, y2[i],))

# Plot 1
plt.plot(x1, y1, 'r.', label="30 pontos",  linewidth=1)
plt.plot(x2, y2, 'b:', label="135 pontos", linewidth=1)
plt.title("Metodo de Euler Implicito")
plt.legend()
plt.grid()
plt.savefig("EulerImplicito.png")
plt.show()


