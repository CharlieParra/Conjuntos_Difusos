import matplotlib.pyplot as plt
import numpy as np

# Función para evaluar una MF gaussiana en 2D:
def MF_gaussian_2D(X, Y, c_x, c_y, sigma_x, sigma_y):
    return np.exp(-(((X - c_x) ** 2) / (2 * sigma_x ** 2) + ((Y - c_y) ** 2) / (2 * sigma_y ** 2)))

# Función para solicitar los valores de los parámetros y el rango del conjunto universo:
def gaussianMF_3D_main():
    c_x = float(input("Ingrese el valor del centro en X (c_x): "))
    c_y = float(input("Ingrese el valor del centro en Y (c_y): "))
    sigma_x = float(input("Ingrese el valor de sigma en X: "))
    sigma_y = float(input("Ingrese el valor de sigma en Y: "))

    while True:
        min_universo_x = float(input("Ingrese el valor mínimo del conjunto universo para X: "))
        max_universo_x = float(input("Ingrese el valor máximo del conjunto universo para X: "))
        min_universo_y = float(input("Ingrese el valor mínimo del conjunto universo para Y: "))
        max_universo_y = float(input("Ingrese el valor máximo del conjunto universo para Y: "))
        if min_universo_x < max_universo_x and min_universo_y < max_universo_y:
            break
        else:
            print("Error: El valor mínimo del conjunto universo debe ser menor al valor máximo para ambos ejes. Por favor, ingrese los valores nuevamente.")

    plot_MF_gaussian_3D(c_x, c_y, sigma_x, sigma_y, min_universo_x, max_universo_x, min_universo_y, max_universo_y)

# Función para graficar la MF gaussiana en 3D:
def plot_MF_gaussian_3D(c_x, c_y, sigma_x, sigma_y, min_universo_x, max_universo_x, min_universo_y, max_universo_y):
    X = np.linspace(min_universo_x, max_universo_x, 500)
    Y = np.linspace(min_universo_y, max_universo_y, 500)
    X, Y = np.meshgrid(X, Y)
    Z = MF_gaussian_2D(X, Y, c_x, c_y, sigma_x, sigma_y)

    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Membership Value')
    ax.set_title('Gaussian Membership Function in 3D')
    plt.show()

# Llamar la función principal
gaussianMF_3D_main()
