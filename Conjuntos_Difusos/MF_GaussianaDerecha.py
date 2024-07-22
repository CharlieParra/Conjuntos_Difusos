# Función para evaluar una MF gaussiana derecha:
# X = Punto de evaluación.
# mid = Punto central de la función de membresía gaussiana.
# sigma = Dispersión de la función de membresía gaussiana.
# min_universo = Valor mínimo del conjunto universo.
# max_universo = Valor máximo del conjunto universo.

import matplotlib.pyplot as plt
import numpy as np

def MF_gaussianaDerecha(X, mid, sigma):
    if X > mid:
        return 1
    else:
        return np.exp(-0.5 * ((X - mid) / sigma) ** 2)

# Función para graficar la MF:
def plot_MF_gaussianaDerecha(mid, sigma, min_universo, max_universo, puntos, color):
    X_values = np.linspace(min_universo, max_universo, puntos)
    X_values = np.concatenate(([mid], X_values))
    X_values = np.sort(X_values)

    MF_values = [MF_gaussianaDerecha(X, mid, sigma) for X in X_values]

    # plt.figure(figsize=(10, 6))
    plt.plot(X_values, MF_values, label=f'Right Gaussian Membership Function (mid={mid}, sigma={sigma})', color=color)

    # plt.xlabel('X')
    # plt.ylabel('Membership Value')
    # plt.title('Right Gaussian Membership Function')
    # plt.legend()
    # plt.grid(True)
    # plt.ylim(-0.1, 1.1)
    # plt.xlim(min_universo, max_universo)
    # plt.show()
