# Función para evaluar una MF gaussiana:
# X = Punto de evaluación.
# mid = Punto central de la función de membresía gaussiana.
# Lsigma = Dispersión de la función de membresía gaussiana del lado izquierdo.
# Rsigma = Dispersión de la función de membresía gaussiana del lado derecho.
# min_universo = Valor mínimo del conjunto universo.
# max_universo = Valor máximo del conjunto universo.

import matplotlib.pyplot as plt
import numpy as np

def MF_gaussianaAsimetrica(X, mid, Lsigma, Rsigma):
    if X <= mid:
        return np.exp(-0.5 * ((X - mid) / Lsigma) ** 2)
    else:
        return np.exp(-0.5 * ((X - mid) / Rsigma) ** 2)

# Función para graficar la MF:
def plot_MF_gaussianaAsimetrica(mid, Lsigma, Rsigma, min_universo, max_universo, puntos, color, negado):
    X_values = np.linspace(min_universo, max_universo, puntos)
    MF_values = [MF_gaussianaAsimetrica(X, mid, Lsigma, Rsigma) for X in X_values]
    
    if negado == 1:
        MF_values = [1 - val for val in MF_values]
        label = f'Gaussiana Negada (mid={mid}, Lsigma={Lsigma}, Rsigma={Rsigma})'
    else:
        label = f'Gaussiana (mid={mid}, Lsigma={Lsigma}, Rsigma={Rsigma})'

    plt.plot(X_values, MF_values, label=label, color=color)
