# Función para evaluar una MF trapezoidal:
# X = Punto de evaluación.
# a = Vértice inferior izquierdo de la función trapezoidal.
# b = Vértice superior izquierdo de la función trapezoidal.
# c = Vértice superior derecho de la función trapezoidal.
# d = Vértice inferior derecho de la función trapezoidal.
# min_universo = Valor mínimo del conjunto universo.
# max_universo = Valor máximo del conjunto universo.

import matplotlib.pyplot as plt
import numpy as np

def MF_trapezoidal(X, a, b, c, d):
    if X <= a:
        return 0
    elif a < X <= b:
        return (X - a) / (b - a)
    elif b < X <= c:
        return 1
    elif c < X < d:
        return (d - X) / (d - c)
    else:
        return 0

# Función para solicitar los valores de a, b, c, d y el rango del conjunto universo:
def tpMF_main():
    while True:
        a = float(input("Ingrese el valor de a: "))
        b = float(input("Ingrese el valor de b: "))
        c = float(input("Ingrese el valor de c: "))
        d = float(input("Ingrese el valor de d: "))
        if a < b < c < d:
            break
        else:
            print("Error: Los valores deben cumplir con la condición a < b < c < d. Por favor, ingrese los valores nuevamente.")

    while True:
        min_universo = float(input("Ingrese el valor mínimo del conjunto universo: "))
        max_universo = float(input("Ingrese el valor máximo del conjunto universo: "))
        if min_universo < max_universo:
            break
        else:
            print("Error: El valor mínimo del conjunto universo debe ser menor al valor máximo. Por favor, ingrese los valores nuevamente.")

    plot_MF_trapezoidal(a, b, c, d, min_universo, max_universo)

# Función para graficar la MF:
def plot_MF_trapezoidal(a, b, c, d, min_universo, max_universo):
    X_values = np.linspace(min_universo, max_universo, 500)
    MF_values = [MF_trapezoidal(X, a, b, c, d) for X in X_values]

    plt.figure(figsize=(10, 6))
    plt.plot(X_values, MF_values, label=f'Trapezoidal Membership Function (a={a}, b={b}, c={c}, d={d})', color='blue')

    plt.xlabel('X')
    plt.ylabel('Membership Value')
    plt.title('Trapezoidal Membership Function')
    plt.legend()
    plt.grid(True)
    plt.ylim(-0.1, 1.1)
    plt.xlim(min_universo, max_universo)
    plt.show()
