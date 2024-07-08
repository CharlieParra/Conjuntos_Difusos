# Función para evaluar una MF triangular:
# X = Punto de evaluación.
# a = Vértice izquierdo de la función triangular.
# b = Vértice central de la función triangular.
# c = Vértice derecho de la función triangular.

import matplotlib.pyplot as plt
import numpy as np

def MF_triangular(X, a, b, c):
    if a <= X <= b:
        return (1 / (b - a)) * (X - a)
    elif b < X <= c:
        return -(1 / (c - b)) * (X - b) + 1
    else:
        return 0

# Función para solicitar los valores de a, b y c para generar su gráfica correspondiente:
def tMF_main():
    a = float(input("Ingrese el valor de a: "))
    b = float(input("Ingrese el valor de b: "))
    c = float(input("Ingrese el valor de c: "))
    plot_MF_triangular(a, b, c)

# Función para graficar la MF:
def plot_MF_triangular(a, b, c):
    X_values = np.linspace(a - 100, c + 100, 500)
    MF_values = [MF_triangular(X, a, b, c) for X in X_values]

    # Generación de los puntos adicionales para los vértices clave
    X_values = np.concatenate(([a, b, c], X_values))
    X_values = np.sort(X_values)
    MF_values = [MF_triangular(X, a, b, c) for X in X_values]

    plt.figure(figsize=(10, 6))
    plt.plot(X_values, MF_values, label=f'Triangular Membership Function (a={a}, b={b}, c={c})', color='blue')

    plt.xlabel('X')
    plt.ylabel('Membership Value')
    plt.title('Triangular Membership Function')
    plt.legend()
    plt.grid(True)
    plt.ylim(-0.1, 1.1)
    plt.xlim(a - 5, c + 5)
    plt.show()
