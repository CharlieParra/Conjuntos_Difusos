# Función para evaluar una MF Izquierda-Derecha (LR):
# X = Punto de evaluación.
# alpha = Define la dispersión de la parte izquierda de la función.
# beta = Define la dispersión de la parte derecha de la función.
# c = Valor del centro de la función.
# min_universo = Valor mínimo del conjunto universo.
# max_universo = Valor máximo del conjunto universo.

import matplotlib.pyplot as plt
import numpy as np

def MF_leftRight(X, c, alpha, beta):
    if X >= c:
        x1 = (X - c) / beta
        return np.exp(-abs(x1**3))
    else:
        x2 = (c - X) / alpha
        return max(0, np.sqrt(1 - x2**2))

# Función para graficar la MF:
def plot_MF_leftRight(c, alpha, beta, min_universo, max_universo, puntos, color):
    X_values = np.linspace(min_universo, max_universo, puntos)
    MF_values = [MF_leftRight(X, c, alpha, beta) for X in X_values]

    # plt.figure(figsize=(10, 6))
    plt.plot(X_values, MF_values, label=f'Triangular Membership Function (alpha={alpha}, beta={beta}, c={c})', color=color)

    # plt.xlabel('X')
    # plt.ylabel('Membership Value')
    # plt.title('Left-Right Membership Function')
    # plt.legend()
    # plt.grid(True)
    # plt.ylim(-0.1, 1.1)
    # plt.xlim(min_universo, max_universo)
    # plt.show()