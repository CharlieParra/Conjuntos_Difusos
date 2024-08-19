# Función para evaluar una MF sigmoidea:
# X = Punto de evaluación.
# a = Valor de la pendiente.
# c = Valor del punto de inflexión.
# min_universo = Valor mínimo del conjunto universo.
# max_universo = Valor máximo del conjunto universo.

import matplotlib.pyplot as plt
import numpy as np

def MF_sigmoidal(X, a, c):
    return 1 / (1 + np.exp(-a * (X - c)))

# Función para graficar la MF
def plot_MF_sigmoidal(a, c, min_universo, max_universo, puntos, color):
    X_values = np.linspace(min_universo, max_universo, puntos)
    MF_values = [MF_sigmoidal(X, a, c) for X in X_values]

    # plt.figure(figsize=(10, 6))
    plt.plot(X_values, MF_values, label=f'Sigmoidal Membership Function (a={a}, c={c})', color=color)

    # plt.xlabel('X')
    # plt.ylabel('Membership Value')
    # plt.title('Sigmoidal Membership Function')
    # plt.legend()
    # plt.grid(True)
    # plt.ylim(-0.1, 1.1)
    # plt.xlim(min_universo, max_universo)
    # plt.show()