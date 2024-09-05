# Función para evaluar una MF trapezoidal:
# X = Punto de evaluación.
# a = Vértice inferior izquierdo de la función trapezoidal.
# b = Vértice superior izquierdo de la función trapezoidal.
# c = Vértice superior derecho de la función trapezoidal.
# d = Vértice inferior derecho de la función trapezoidal.
# min_universo = Valor mínimo del conjunto universo.
# max_universo = Valor máximo del conjunto universo.

import matplotlib.pyplot as plt
import numpy as np

def MF_trapezoidal(X, a, b, c, d):
    if X <= a:
        return 0
    elif a < X <= b:
        return (X - a) / (b - a)
    elif b < X <= c:
        return 1
    elif c < X < d:
        return (d - X) / (d - c)
    else:
        return 0

# Función para graficar la MF:
def plot_MF_trapezoidal(a, b, c, d, min_universo, max_universo, puntos, color, negado):
    X_values = np.linspace(min_universo, max_universo, puntos)
    MF_values = [MF_trapezoidal(X, a, b, c, d) for X in X_values]
    
    if negado == 1:
        MF_values = [1 - val for val in MF_values]
        label = f'Trapezoidal Negada (a={a}, b={b}, c={c}, d={d})'
    else:
        label = f'Trapezoidal (a={a}, b={b}, c={c}, d={d})'

    plt.plot(X_values, MF_values, label=label, color=color)
