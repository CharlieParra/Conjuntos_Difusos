# Función para evaluar una MF campana generalizada:
# X = Punto de evaluación.
# a = Valor del ancho.
# b = Valor del parámetro de forma.
# c = Valor del centro.
# min_universo = Valor mínimo del conjunto universo.
# max_universo = Valor máximo del conjunto universo.

import matplotlib.pyplot as plt
import numpy as np

def MF_generalizedBell(X, c, a, b):
    return 1 / (1 + abs((X - c) / a) ** (2 * b))

# Función para graficar la MF:
def plot_MF_generalizedBell(c, a, b, min_universo, max_universo, puntos, color, negado):
    X_values = np.linspace(min_universo, max_universo, puntos)
    MF_values = [MF_generalizedBell(X, c, a, b) for X in X_values]
    
    if negado == 1:
        MF_values = [1 - val for val in MF_values]
        label = f'Cauchy Negada (c={c}, a={a}, b={b})'
    else:
        label = f'Cauchy (c={c}, a={a}, b={b})'

    plt.plot(X_values, MF_values, label=label, color=color)
