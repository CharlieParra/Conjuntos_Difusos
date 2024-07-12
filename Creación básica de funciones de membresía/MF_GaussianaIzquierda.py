# Función para evaluar una MF gaussiana izquierda:
# X = Punto de evaluación.
# mid = Punto central de la función de membresía gaussiana.
# sigma = Dispersión de la función de membresía gaussiana.

import matplotlib.pyplot as plt
import numpy as np

def MF_gaussianaIzquierda(X, mid, sigma):
    if X <= mid:
        return 1
    else:
        return np.exp(-0.5 * ((X - mid) / sigma) ** 2)

# Función para solicitar los valores de mid y sigma para generar su gráfica correspondiente:
def lgMF_main():
    mid = float(input("Ingrese el valor del centro (mid): "))
    sigma = float(input("Ingrese el valor de la dispersión (sigma): "))
    plot_MF_gaussianaIzquierda(mid, sigma)

# Función para graficar la MF:
def plot_MF_gaussianaIzquierda(mid, sigma):
    X_values = np.linspace(mid - 10 * sigma, mid + 10 * sigma, 500)
    MF_values = [MF_gaussianaIzquierda(X, mid, sigma) for X in X_values]

    plt.figure(figsize=(10, 6))
    plt.plot(X_values, MF_values, label=f'Left Gaussian Membership Function (mid={mid}, sigma={sigma})', color='blue')

    plt.xlabel('X')
    plt.ylabel('Membership Value')
    plt.title('Left Gaussian Membership Function')
    plt.legend()
    plt.grid(True)
    plt.ylim(-0.1, 1.1)
    plt.xlim(mid - 5 * sigma, mid + 5 * sigma)
    plt.show()
