import matplotlib.pyplot as plt
import numpy as np

# Función para evaluar una MF trapezoidal en 2D:
def MF_trapezoidal_2D(X, Y, a, b, c, d):
    def trapezoidal(x, a, b, c, d):
        if x <= a:
            return 0
        elif a < x <= b:
            return (x - a) / (b - a)
        elif b < x <= c:
            return 1
        elif c < x <= d:
            return (d - x) / (d - c)
        else:
            return 0

    Z = np.zeros(X.shape)
    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            Z[i, j] = min(trapezoidal(X[i, j], a[0], b[0], c[0], d[0]), 
                          trapezoidal(Y[i, j], a[1], b[1], c[1], d[1]))
    return Z

# Función para solicitar los valores de los parámetros y el rango del conjunto universo:
def trapezoidalMF_3D_main():
    a_x = float(input("Ingrese el valor de a en X: "))
    b_x = float(input("Ingrese el valor de b en X: "))
    c_x = float(input("Ingrese el valor de c en X: "))
    d_x = float(input("Ingrese el valor de d en X: "))

    a_y = float(input("Ingrese el valor de a en Y: "))
    b_y = float(input("Ingrese el valor de b en Y: "))
    c_y = float(input("Ingrese el valor de c en Y: "))
    d_y = float(input("Ingrese el valor de d en Y: "))

    while True:
        min_universo_x = float(input("Ingrese el valor mínimo del conjunto universo para X: "))
        max_universo_x = float(input("Ingrese el valor máximo del conjunto universo para X: "))
        min_universo_y = float(input("Ingrese el valor mínimo del conjunto universo para Y: "))
        max_universo_y = float(input("Ingrese el valor máximo del conjunto universo para Y: "))
        if min_universo_x < max_universo_x and min_universo_y < max_universo_y:
            break
        else:
            print("Error: El valor mínimo del conjunto universo debe ser menor al valor máximo para ambos ejes. Por favor, ingrese los valores nuevamente.")

    plot_MF_trapezoidal_3D([a_x, a_y], [b_x, b_y], [c_x, c_y], [d_x, d_y], min_universo_x, max_universo_x, min_universo_y, max_universo_y)

# Función para graficar la MF trapezoidal en 3D:
def plot_MF_trapezoidal_3D(a, b, c, d, min_universo_x, max_universo_x, min_universo_y, max_universo_y):
    X = np.linspace(min_universo_x, max_universo_x, 500)
    Y = np.linspace(min_universo_y, max_universo_y, 500)
    X, Y = np.meshgrid(X, Y)
    Z = MF_trapezoidal_2D(X, Y, a, b, c, d)

    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Membership Value')
    ax.set_title('Trapezoidal Membership Function in 3D')
    plt.show()

# Llamar la función principal
trapezoidalMF_3D_main()