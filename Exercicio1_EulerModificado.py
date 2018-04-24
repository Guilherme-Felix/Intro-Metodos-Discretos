import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize 

'''
Implementacao do metodo de euler modificado, segundo a ref.
https://www.ufrgs.br/reamat/CalculoNumerico/livro-py/pdvi-metodo_de_euler_melhorado.html
'''

interval = (0,1)
h = 1./30

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

def f(Y):
    return np.arctan(Y)

# Metodo de Euler Modificado - 30 -pontos
for k in range(N1-1):
    yk = y1[k] + h1*f(y1[k]) 
    y1[k+1] = y1[k] + (h1/2)*( f(y1[k]) + f(yk))

# Metodo de Euler Modificado - 135 -pontos
for k in range(N2-1):
    yk = y2[k] + h2*f(y2[k]) 
    y2[k+1] = y2[k] + (h2/2)*( f(y2[k]) + f(yk))

# Plot do grafico
plt.plot(x1, y1, 'r.', label="30 pontos",  linewidth=1)
plt.plot(x2, y2, 'b:', label="135 pontos", linewidth=1)
plt.title("Metodo de Euler Modificado")
plt.legend()
plt.grid()
plt.savefig("Euler_modificado.png")
plt.show()
