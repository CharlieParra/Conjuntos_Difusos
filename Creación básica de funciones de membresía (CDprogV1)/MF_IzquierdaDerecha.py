# Función para evaluar una MF Izquierda-Derecha (LR):
# X = Punto de evaluación.
# alpha = Define la dispersión de la parte izquierda de la función.
# beta = Define la dispersión de la parte derecha de la función.
# c = Valor del centro de la función.
# min_universo = Valor mínimo del conjunto universo.
# max_universo = Valor máximo del conjunto universo.

import matplotlib.pyplot as plt
import numpy as np

def MF_leftRight(X, alpha, beta, c):
    if X >= c:
        x1 = (X - c) / beta
        return np.exp(-abs(x1**3))
    else:
        x2 = (c - X) / alpha
        return max(0, np.sqrt(1 - x2**2))

# Función para solicitar los valores de c, a, b y el rango del conjunto universo:
def lrMF_main():
    c = float(input("Ingrese el valor del centro (c): "))
    alpha = float(input("Ingrese el valor de alpha: "))
    beta = float(input("Ingrese el valor de beta: "))

    while True:
        min_universo = float(input("Ingrese el valor mínimo del conjunto universo: "))
        max_universo = float(input("Ingrese el valor máximo del conjunto universo: "))
        if min_universo < max_universo:
            break
        else:
            print("Error: El valor mínimo del conjunto universo debe ser menor al valor máximo. Por favor, ingrese los valores nuevamente.")

    plot_MF_leftRight(alpha, beta, c, min_universo, max_universo)

# Función para graficar la MF:
def plot_MF_leftRight(alpha, beta, c, min_universo, max_universo):
    X_values = np.linspace(min_universo, max_universo, 500)
    MF_values = [MF_leftRight(X, alpha, beta, c) for X in X_values]

    plt.figure(figsize=(10, 6))
    plt.plot(X_values, MF_values, label=f'Triangular Membership Function (alpha={alpha}, beta={beta}, c={c})', color='blue')

    plt.xlabel('X')
    plt.ylabel('Membership Value')
    plt.title('Left-Right Membership Function')
    plt.legend()
    plt.grid(True)
    plt.ylim(-0.1, 1.1)
    plt.xlim(min_universo, max_universo)
    plt.show()
