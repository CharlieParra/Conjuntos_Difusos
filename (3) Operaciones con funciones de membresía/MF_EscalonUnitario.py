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
def plot_MF_escalonUnitario(a, min_universo, max_universo, puntos, color, negado):
    X_values = np.linspace(a - 0.000000001, a + 0.000000001, puntos)
    MF_values = [MF_escalonUnitario(X, a) for X in X_values]
    
    if negado == 1:
        MF_values = [1 - val for val in MF_values]
        label = f'Escalón Negado (a={a})'
    else:
        label = f'Escalón (a={a})'

    plt.plot(X_values, MF_values, label=label, color=color)
