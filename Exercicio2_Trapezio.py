import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize 

'''
    Universidade Federal de Juiz de Fora
    Departamento de Mecanica Aplicada e Computacional - MAC
    MAC026 - Introducao aos Metodos Discretos
    Guilherme Almeida Felix da Silva - 201365504B
    guilherme.felix@engenharia.ufjf.br
    
    Exercicio: Resolver pelo metodo de Euler Implicito
    y' = y^2 - g(x), onde:
    
    g(x) = x^4 - 6x^3 + 12x^2 - 14x +9
    y(0) = 2
    h1 = 0.2
    h2 = 0.1
    h3 = 0.05
    x E [0, 1.6]
'''

# Passo em cada caso
h1 = 0.2
h2 = 0.1
h3 = 0.05

# Numero de pontos
N1 = int (1.6 / h1)
N2 = int (1.6 / h2)
N3 = int (1.6 / h3)

# Dominio. [0, 1.6]
x1 = np.arange(0,1.6,h1)
x2 = np.arange(0,1.6,h2)
x3 = np.arange(0,1.6,h3)

# Vetor que guarda as solucoes
y1 = np.zeros(N1)
y2 = np.zeros(N2)
y3 = np.zeros(N3)

# Condicao Inicial
y1[0] = 2
y2[0] = 2
y3[0] = 2

def g(x):
    return (x**4 - 6*(x**3) + 12*(x**2) - 14*x + 9) / (1 + x)**2

def f(y,x):
    return y**2 - g(x)

def F(Y, h, yk, x):
    return Y - (h/2)* ( f(Y,x) + f(yk,x) ) - yk 

def Fprime(Y, h, y, x):
    return 1 - (h*y)  

def SolucaoExata(x):
    return ((1 - x)*(2 - x) / (1 + x))

# Metodo do Trapezio - h = 0.2
for i in range(N1-1):
    y1[i+1] = optimize.newton(F, y1[i], fprime=Fprime, args=(h1, y1[i],x1[i]))

# Metodo do Trapezio - h = 0.1
for i in range(N2-1):
    y2[i+1] = optimize.newton(F, y2[i], fprime=Fprime, args=(h2, y2[i],x2[i]))

# Metodo do Trapezio - h = 0.05
for i in range(N3-1):
    y3[i+1] = optimize.newton(F, y3[i], fprime=Fprime, args=(h3, y3[i],x3[i]))

# Plota a saida
plt.plot(x1, y1, 'r.', label="h1 = 0.2",  linewidth=1)
plt.plot(x2, y2, 'b:', label="h2 = 0.1", linewidth=1)
plt.plot(x3, y3, 'g-', label="h3 = 0.05", linewidth=1)
plt.plot(x3, SolucaoExata(x3), 'k', label="Solucao Exata", linewidth=1)
plt.title("Metodo do Trapezio")
plt.legend()
plt.grid()
plt.savefig("Ex2_Trapezio.png")
plt.show()
