# Función para evaluar una MF escalón unitario:
# X = Punto de evaluación.
# a = Punto de flanco de subida.
# min_universo = Valor mínimo del conjunto universo.
# max_universo = Valor máximo del conjunto universo.

import matplotlib.pyplot as plt
import numpy as np

def MF_escalonUnitario(X, a):
    return 1 if X >= a else 0

# Función para graficar la MF:
def plot_MF_escalonUnitario(a, min_universo, max_universo, puntos, color):
    X_values = np.linspace(a - 0.000000001, a + 0.000000001, puntos)
    MF_values = [MF_escalonUnitario(X, a) for X in X_values]

    # plt.figure(figsize=(10, 6))
    plt.plot(X_values, MF_values, label=f'Step Membership Function (a={a})', color=color)

    # plt.xlabel('X')
    # plt.ylabel('Membership Value')
    # plt.title('Step Membership Function - Flanco de Subida')
    # plt.legend()
    # plt.grid(True)
    # plt.ylim(-0.1, 1.1)
    # plt.xlim(min_universo, max_universo)
    # plt.show()