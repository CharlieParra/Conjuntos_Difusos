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
def plot_MF_triangularDerecha(a, b, min_universo, max_universo, puntos, color):
    X_values = np.linspace(min_universo, max_universo, puntos)
    X_values = np.concatenate(([a, b], X_values))
    X_values = np.sort(X_values)

    MF_values = [MF_triangularDerecha(X, a, b) for X in X_values]

    # plt.figure(figsize=(10, 6))
    # plt.plot(X_values, MF_values, label=f'Triangular Membership Function (a={a}, b={b})', color='blue')
    plt.plot(X_values, MF_values, label=f'Triangular Membership Function (a={a}, b={b})', color=color)

    # plt.xlabel('X')
    # plt.ylabel('Membership Value')
    # plt.title('Right Triangular Membership Function')
    # plt.legend()
    # plt.grid(True)
    # plt.ylim(-0.1, 1.1)
    # plt.xlim(min_universo, max_universo)
    # plt.show()