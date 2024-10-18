import matplotlib.pyplot as plt
import numpy as np

# Función para evaluar la MF Izquierda-Derecha en 2D:
def MF_leftRight_2D(X, Y, alpha, beta, c):
    Z = np.zeros_like(X)
    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            if X[i, j] >= c:
                x1 = (X[i, j] - c) / beta
                Z[i, j] = np.exp(-abs(x1**3))
            else:
                x2 = (c - X[i, j]) / alpha
                Z[i, j] = max(0, np.sqrt(1 - x2**2))
    return Z

# Función para solicitar los valores de los parámetros y el rango del conjunto universo:
def leftRightMF_3D_main():
    alpha = float(input("Ingrese el valor del parámetro alpha (define la dispersión izquierda): "))
    beta = float(input("Ingrese el valor del parámetro beta (define la dispersión derecha): "))
    c = float(input("Ingrese el valor del centro c: "))

    while True:
        min_universo_x = float(input("Ingrese el valor mínimo del conjunto universo para X: "))
        max_universo_x = float(input("Ingrese el valor máximo del conjunto universo para X: "))
        min_universo_y = float(input("Ingrese el valor mínimo del conjunto universo para Y: "))
        max_universo_y = float(input("Ingrese el valor máximo del conjunto universo para Y: "))
        if min_universo_x < max_universo_x and min_universo_y < max_universo_y:
            break
        else:
            print("Error: El valor mínimo del conjunto universo debe ser menor al valor máximo para ambos ejes. Por favor, ingrese los valores nuevamente.")

    plot_MF_leftRight_3D(alpha, beta, c, min_universo_x, max_universo_x, min_universo_y, max_universo_y)

# Función para graficar la MF Izquierda-Derecha en 3D:
def plot_MF_leftRight_3D(alpha, beta, c, min_universo_x, max_universo_x, min_universo_y, max_universo_y):
    X = np.linspace(min_universo_x, max_universo_x, 500)
    Y = np.linspace(min_universo_y, max_universo_y, 500)
    X, Y = np.meshgrid(X, Y)
    Z = MF_leftRight_2D(X, Y, alpha, beta, c)

    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Membership Value')
    ax.set_title('Left-Right Membership Function in 3D')
    plt.show()
