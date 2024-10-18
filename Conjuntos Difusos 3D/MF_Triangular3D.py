import matplotlib.pyplot as plt
import numpy as np

# Función para evaluar una MF triangular en 2D:
def MF_triangular_2D(X, Y, a, b, c, d, e, f):
    Z = np.zeros_like(X)
    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            if X[i, j] <= a or Y[i, j] <= d:
                Z[i, j] = 0
            elif a < X[i, j] <= b and d < Y[i, j] <= e:
                Z[i, j] = min((X[i, j] - a) / (b - a), (Y[i, j] - d) / (e - d))
            elif b < X[i, j] < c and e < Y[i, j] < f:
                Z[i, j] = min(-(X[i, j] - c) / (c - b), -(Y[i, j] - f) / (f - e))
            else:
                Z[i, j] = 0
    return Z

# Función para solicitar los valores de los parámetros y el rango del conjunto universo:
def tnMF_3D_main():
    while True:
        a = float(input("Ingrese el valor de a (para X): "))
        b = float(input("Ingrese el valor de b (para X): "))
        c = float(input("Ingrese el valor de c (para X): "))
        if a < b < c:
            break
        else:
            print("Error: El valor de a debe ser menor que b y el valor de b debe ser menor que c. Por favor, ingrese los valores nuevamente.")

    while True:
        d = float(input("Ingrese el valor de d (para Y): "))
        e = float(input("Ingrese el valor de e (para Y): "))
        f = float(input("Ingrese el valor de f (para Y): "))
        if d < e < f:
            break
        else:
            print("Error: El valor de d debe ser menor que e y el valor de e debe ser menor que f. Por favor, ingrese los valores nuevamente.")

    while True:
        min_universo_x = float(input("Ingrese el valor mínimo del conjunto universo para X: "))
        max_universo_x = float(input("Ingrese el valor máximo del conjunto universo para X: "))
        min_universo_y = float(input("Ingrese el valor mínimo del conjunto universo para Y: "))
        max_universo_y = float(input("Ingrese el valor máximo del conjunto universo para Y: "))
        if min_universo_x < max_universo_x and min_universo_y < max_universo_y:
            break
        else:
            print("Error: El valor mínimo del conjunto universo debe ser menor al valor máximo para ambos ejes. Por favor, ingrese los valores nuevamente.")

    plot_MF_triangular_3D(a, b, c, d, e, f, min_universo_x, max_universo_x, min_universo_y, max_universo_y)

# Función para graficar la MF en 3D:
def plot_MF_triangular_3D(a, b, c, d, e, f, min_universo_x, max_universo_x, min_universo_y, max_universo_y):
    X = np.linspace(min_universo_x, max_universo_x, 500)
    Y = np.linspace(min_universo_y, max_universo_y, 500)
    X, Y = np.meshgrid(X, Y)
    Z = MF_triangular_2D(X, Y, a, b, c, d, e, f)

    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Membership Value')
    ax.set_title('Triangular Membership Function in 3D')
    plt.show()
