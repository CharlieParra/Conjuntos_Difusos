# Función para evaluar una MF triangular:
# X = Punto de evaluación.
# a = Vértice izquierdo de la función triangular.
# b = Vértice central de la función triangular.
# c = Vértice derecho de la función triangular.
# min_universo = Valor mínimo del conjunto universo.
# max_universo = Valor máximo del conjunto universo.

import matplotlib.pyplot as plt
import numpy as np

def MF_triangular(X, a, b, c):
    if X <= a:
        return 0
    elif a < X <= b:
        return (1 / (b - a)) * (X - a)
    elif b < X < c:
        return -(1 / (c - b)) * (X - c)
    else:
        return 0

# Función para graficar la MF:
def plot_MF_triangular(a, b, c, min_universo, max_universo, puntos, color, negado):
    X_values = np.linspace(min_universo, max_universo, puntos)
    X_values = np.concatenate(([a, b, c], X_values))
    X_values = np.sort(X_values)

    MF_values = [MF_triangular(X, a, b, c) for X in X_values]

    if negado == 1:
        MF_values = [1 - val for val in MF_values]
        label = f'Triangular Negada (a={a}, b={b}, c={c})'
    else:
        label = f'Triangular (a={a}, b={b}, c={c})'

    plt.plot(X_values, MF_values, label=label, color=color)
