import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize 
'''
    Universidade Federal de Juiz de Fora
    Departamento de Mecanica Aplicada e Computacional - MAC
    MAC026 - Introducao aos Metodos Discretos
    Guilherme Almeida Felix da Silva - 201365504B
    guilherme.felix@engenharia.ufjf.br
    
    Exercicio: Resolver pelo metodo de Euler Explicito
    y' = y^2 - g(x), onde:
    
    g(x) = x^4 - 6x^3 + 12x^2 - 14x +9
    y(0) = 2
    h1 = 0.2
    h2 = 0.1
    h3 = 0.05
    x E [0, 1.6]
'''
# Numero de pontos 
N1 = 30 
N2 = 135

# Tamanho do passo
h1 = 1./N1
h2 = 1./N2

# Dominio [0, 1]
x1 = np.arange(0,1,h1)
x2 = np.arange(0,1,h2)

# Vetor que guarda as solucoes
y1 = np.zeros(N1)
y2 = np.zeros(N2)

# Condicao Inicial
y1[0] = 1
y2[0] = 1

def F(Y, h, yk):
    return Y - h*np.arctan(Y) - yk

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


