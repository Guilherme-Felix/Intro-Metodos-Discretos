import numpy as np
import matplotlib.pyplot as plt
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

# Passo 
h1 = 1./N1
h2 = 1./N2

# Dominio, [0,1]
x1 = np.arange(0,1,h1)
x2 = np.arange(0,1,h2)

# Vetor que guarda as solucoes
y1 = np.zeros(N1)
y2 = np.zeros(N2)

# Condicao Inicial
y1[0] = 1
y2[0] = 1

def f(x):
    return np.arctan(x)

# Solucao para h1
for i in range(N1-1):
    y1[i+1] = y1[i] + h1*( f(y1[i]) )

# Solucao para h2
for i in range(N2-1):
    y2[i+1] = y2[i] + h2*( f(y2[i]) )

# Plota a saida
plt.plot(x1, y1, 'r.', label="30 pontos",  linewidth=1)
plt.plot(x2, y2, 'b:', label="135 pontos", linewidth=1)
plt.title("Metodo de Euler Explicito")
plt.legend()
plt.grid()
plt.savefig("EulerExplicito.png")
plt.show()


