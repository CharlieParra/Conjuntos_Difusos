import matplotlib.pyplot as plt
import numpy as np

def MF_generalizedBell(X, c, a, b):
    return 1 / (1 + abs((X - c) / a) ** (2 * b))

# Función para solicitar los valores de c, a, b y el rango del conjunto universo:
def gbMF_main():
    c = float(input("Ingrese el valor del centro (c): "))
    a = float(input("Ingrese el valor del ancho (a): "))
    b = float(input("Ingrese el valor del parámetro de forma (b): "))

    while True:
        min_universo = float(input("Ingrese el valor mínimo del conjunto universo: "))
        max_universo = float(input("Ingrese el valor máximo del conjunto universo: "))
        if min_universo < max_universo:
            break
        else:
            print("Error: El valor mínimo del conjunto universo debe ser menor al valor máximo. Por favor, ingrese los valores nuevamente.")

    plot_MF_generalizedBell(c, a, b, min_universo, max_universo)

# Función para graficar la MF:
def plot_MF_generalizedBell(c, a, b, min_universo, max_universo):
    X_values = np.linspace(min_universo, max_universo, 500)
    MF_values = [MF_generalizedBell(X, c, a, b) for X in X_values]

    plt.figure(figsize=(10, 6))
    plt.plot(X_values, MF_values, label=f'Generalized Bell MF (c={c}, a={a}, b={b})', color='blue')

    plt.xlabel('X')
    plt.ylabel('Membership Value')
    plt.title('Generalized Bell Membership Function')
    plt.legend()
    plt.grid(True)
    plt.ylim(-0.1, 1.1)
    plt.xlim(min_universo, max_universo)
    plt.show()

# Ejecutar la función principal para solicitar valores y graficar
gbMF_main()
