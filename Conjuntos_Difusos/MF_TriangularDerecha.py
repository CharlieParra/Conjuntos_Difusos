# Función para evaluar una MF triangular derecha:
# X = Punto de evaluación.
# a = Vértice izquierdo de la función triangular.
# b = Vértice derecho de la función triangular.
# min_universo = Valor mínimo del conjunto universo.
# max_universo = Valor máximo del conjunto universo.

import matplotlib.pyplot as plt
import numpy as np

def MF_triangularDerecha(X, a, b):
    if X <= a:
        return 0
    elif a < X < b:
        return (1 / (b - a)) * (X - a)
    else:
        return 1

# Función para graficar la MF:
def plot_MF_triangularDerecha(a, b, min_universo, max_universo, puntos, color, negado):
    X_values = np.linspace(min_universo, max_universo, puntos)
    X_values = np.concatenate(([a, b], X_values))
    X_values = np.sort(X_values)

    MF_values = [MF_triangularDerecha(X, a, b) for X in X_values]
    
    if negado == 1:
        MF_values = [1 - val for val in MF_values]
        label = f'Triangular Negada (a={a}, b={b})'
    else:
        label = f'Triangular (a={a}, b={b})'
    
    plt.plot(X_values, MF_values, label=label, color=color)
