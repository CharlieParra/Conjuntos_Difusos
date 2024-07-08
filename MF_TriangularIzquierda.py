# Función para evaluar una MF triangular izquierda:
# X = Punto de evaluación.
# a = Vértice izquierdo de la función triangular.
# b = Vértice derecho de la función triangular.

import matplotlib.pyplot as plt
import numpy as np

def MF_triangularIzquierda(X, a, b):
    if X <= a:
        return 1
    elif a < X < b:
        return -(1 / (b - a)) * (X - a) + 1
    else:
        return 0

# Función para solicitar los valores de a y b para generar su gráfica correspondiente:
def ltMF_main():
    a = float(input("Ingrese el valor de a: "))
    b = float(input("Ingrese el valor de b: "))
    plot_MF_triangularIzquierda(a, b)

# Función para graficar la MF:
def plot_MF_triangularIzquierda(a, b):
    X_values = np.linspace(a - 100, b + 100, 500)
    MF_values = [MF_triangularIzquierda(X, a, b) for X in X_values]

    # Generación de los puntos adicionales para los vértices clave:
    X_values = np.concatenate(([a, b], X_values))
    X_values = np.sort(X_values)
    MF_values = [MF_triangularIzquierda(X, a, b) for X in X_values]

    plt.figure(figsize=(10, 6))
    plt.plot(X_values, MF_values, label=f'Triangular Membership Function (a={a}, b={b})', color='blue')

    plt.xlabel('X')
    plt.ylabel('Membership Value')
    plt.title('Left Triangular Membership Function')
    plt.legend()
    plt.grid(True)
    plt.ylim(-0.1, 1.1)
    plt.xlim(a - 5, b + 5)
    plt.show()
