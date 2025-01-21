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
def plot_MF_gaussianaDerecha(mid, sigma, min_universo, max_universo, puntos, color, negado):
    X_values = np.linspace(min_universo, max_universo, puntos)
    X_values = np.concatenate(([mid], X_values))
    X_values = np.sort(X_values)

    MF_values = [MF_gaussianaDerecha(X, mid, sigma) for X in X_values]
    
    if negado == 1:
        MF_values = [1 - val for val in MF_values]
        label = f'Gaussiana Negada (mid={mid}, sigma={sigma})'
    else:
        label = f'Gaussiana (mid={mid}, sigma={sigma})'

    plt.plot(X_values, MF_values, label=label, color=color)
