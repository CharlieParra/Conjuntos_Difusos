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
def plot_MF_sigmoidal(a, c, min_universo, max_universo, puntos, color, negado):
    X_values = np.linspace(min_universo, max_universo, puntos)
    MF_values = [MF_sigmoidal(X, a, c) for X in X_values]
    
    if negado == 1:
        MF_values = [1 - val for val in MF_values]
        label = f'Sigmoide Negada (a={a}, c={c})'
    else:
        label = f'Sigmoide (a={a}, c={c})'

    plt.plot(X_values, MF_values, label=label, color=color)