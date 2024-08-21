import matplotlib.pyplot as plt
import numpy as np

# Función para evaluar la MF de Cauchy (campana generalizada) en 2D:
def MF_cauchy_2D(X, Y, a, b, c_x, c_y):
    Z = 1 / (1 + ((X - c_x) / a)**2 + ((Y - c_y) / b)**2)
    return Z

# Función para solicitar los valores de los parámetros y el rango del conjunto universo:
def cauchyMF_3D_main():
    a = float(input("Ingrese el valor del parámetro a (controla la anchura en X): "))
    b = float(input("Ingrese el valor del parámetro b (controla la anchura en Y): "))
    c_x = float(input("Ingrese el valor del centro c_x en X: "))
    c_y = float(input("Ingrese el valor del centro c_y en Y: "))

    while True:
        min_universo_x = float(input("Ingrese el valor mínimo del conjunto universo para X: "))
        max_universo_x = float(input("Ingrese el valor máximo del conjunto universo para X: "))
        min_universo_y = float(input("Ingrese el valor mínimo del conjunto universo para Y: "))
        max_universo_y = float(input("Ingrese el valor máximo del conjunto universo para Y: "))
        if min_universo_x < max_universo_x and min_universo_y < max_universo_y:
            break
        else:
            print("Error: El valor mínimo del conjunto universo debe ser menor al valor máximo para ambos ejes. Por favor, ingrese los valores nuevamente.")

    plot_MF_cauchy_3D(a, b, c_x, c_y, min_universo_x, max_universo_x, min_universo_y, max_universo_y)

# Función para graficar la MF de Cauchy en 3D:
def plot_MF_cauchy_3D(a, b, c_x, c_y, min_universo_x, max_universo_x, min_universo_y, max_universo_y):
    X = np.linspace(min_universo_x, max_universo_x, 500)
    Y = np.linspace(min_universo_y, max_universo_y, 500)
    X, Y = np.meshgrid(X, Y)
    Z = MF_cauchy_2D(X, Y, a, b, c_x, c_y)

    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Membership Value')
    ax.set_title('Cauchy (Generalized Bell) Membership Function in 3D')
    plt.show()

# Llamar la función principal
cauchyMF_3D_main()
