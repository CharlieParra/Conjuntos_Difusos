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
def plot_MF_generalizedBell(c, a, b, min_universo, max_universo, puntos, color):
    X_values = np.linspace(min_universo, max_universo, puntos)
    MF_values = [MF_generalizedBell(X, c, a, b) for X in X_values]

    # plt.figure(figsize=(10, 6))
    plt.plot(X_values, MF_values, label=f'Generalized Bell MF (c={c}, a={a}, b={b})', color=color)

    # plt.xlabel('X')
    # plt.ylabel('Membership Value')
    # plt.title('Generalized Bell Membership Function')
    # plt.legend()
    # plt.grid(True)
    # plt.ylim(-0.1, 1.1)
    # plt.xlim(min_universo, max_universo)
    # plt.show()
