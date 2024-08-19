import matplotlib.pyplot as plt
import numpy as np

# Función para evaluar una MF sigmoidal
def MF_sigmoidal(X, a, c):
    return 1 / (1 + np.exp(-a * (X - c)))

# Función para solicitar los valores de a, c y el rango del conjunto universo:
def sigMF_main():
    c = float(input("Ingrese el valor del punto de inflexión (c): "))
    a = float(input("Ingrese el valor de la pendiente (a): "))

    while True:
        min_universo = float(input("Ingrese el valor mínimo del conjunto universo: "))
        max_universo = float(input("Ingrese el valor máximo del conjunto universo: "))
        if min_universo < max_universo:
            break
        else:
            print("Error: El valor mínimo del conjunto universo debe ser menor al valor máximo. Por favor, ingrese los valores nuevamente.")

    plot_MF_sigmoidal(a, c, min_universo, max_universo)

# Función para graficar la MF:
def plot_MF_sigmoidal(a, c, min_universo, max_universo):
    X_values = np.linspace(min_universo, max_universo, 500)
    MF_values = [MF_sigmoidal(X, a, c) for X in X_values]

    plt.figure(figsize=(10, 6))
    plt.plot(X_values, MF_values, label=f'Sigmoidal Membership Function (a={a}, c={c})', color='blue')

    plt.xlabel('X')
    plt.ylabel('Membership Value')
    plt.title('Sigmoidal Membership Function')
    plt.legend()
    plt.grid(True)
    plt.ylim(-0.1, 1.1)
    plt.xlim(min_universo, max_universo)
    plt.show()

# Ejecutar la función principal para solicitar valores y graficar
sigMF_main()
