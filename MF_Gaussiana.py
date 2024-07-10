# Función para evaluar una MF gaussiana:
# X = Punto de evaluación.
# mid = Punto central de la función de membresía gaussiana.
# sigma = Dispersión de la función de membresía gaussiana.
# min_universo = Valor mínimo del conjunto universo.
# max_universo = Valor máximo del conjunto universo.

import matplotlib.pyplot as plt
import numpy as np

def MF_gaussianaAsimetrica(X, mid, Lsigma, Rsigma):
    if X <= mid:
        return np.exp(-0.5 * ((X - mid) / Lsigma) ** 2)
    else:
        return np.exp(-0.5 * ((X - mid) / Rsigma) ** 2)

# Función para solicitar los valores de mid, Lsigma, Rsigma y el rango del conjunto universo:
def agMF_main():
    mid = float(input("Ingrese el valor del centro (mid): "))
    Lsigma = float(input("Ingrese el valor de la desviación estándar izquierda (Lsigma): "))
    Rsigma = float(input("Ingrese el valor de la desviación estándar derecha (Rsigma): "))

    while True:
        min_universo = float(input("Ingrese el valor mínimo del conjunto universo: "))
        max_universo = float(input("Ingrese el valor máximo del conjunto universo: "))
        if min_universo < max_universo:
            break
        else:
            print("Error: El valor mínimo del conjunto universo debe ser menor al valor máximo. Por favor, ingrese los valores nuevamente.")

    plot_MF_gaussianaAsimetrica(mid, Lsigma, Rsigma, min_universo, max_universo)

# Función para graficar la MF:
def plot_MF_gaussianaAsimetrica(mid, Lsigma, Rsigma, min_universo, max_universo):
    X_values = np.linspace(min_universo, max_universo, 500)
    MF_values = [MF_gaussianaAsimetrica(X, mid, Lsigma, Rsigma) for X in X_values]

    plt.figure(figsize=(10, 6))
    plt.plot(X_values, MF_values, label=f'Asymmetric Gaussian MF (mid={mid}, Lsigma={Lsigma}, Rsigma={Rsigma})', color='blue')

    plt.xlabel('X')
    plt.ylabel('Membership Value')
    plt.title('Asymmetric Gaussian Membership Function')
    plt.legend()
    plt.grid(True)
    plt.ylim(-0.1, 1.1)
    plt.xlim(min_universo, max_universo)
    plt.show()
