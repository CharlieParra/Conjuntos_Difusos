import matplotlib.pyplot as plt
import numpy as np

resultados = []
calculos = []
colores = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black', 'orange', 'purple', 'brown']

# Función para solicitar los valores de a, b, c de la función triangular:
def tnMF_main(auto, A, B, C, retorno, puntos):
    while True:
        if not auto:
            a = float(input("Ingrese el valor de a: "))
            b = float(input("Ingrese el valor de b: "))
            c = float(input("Ingrese el valor de c: "))
        else:
            a = A
            b = B
            c = C

        if a < b < c:
            break
        else:
            print("Error: El valor de a debe ser menor que b y el valor de b debe ser menor que c. Por favor, ingrese los valores nuevamente.")

    return [1, a, b, c, puntos, 0]

# Función para evaluar una MF triangular:
def MF_triangular(X, a, b, c):
    if X <= a:
        return 0
    elif a < X <= b:
        return (1 / (b - a)) * (X - a)
    elif b < X < c:
        return -(1 / (c - b)) * (X - c)
    else:
        return 0

# Función para graficar la MF:
def plot_MF_triangular(a, b, c, min_universo, max_universo, puntos, color, negado):
    X_values = np.linspace(min_universo, max_universo, puntos)
    X_values = np.concatenate(([a, b, c], X_values))
    X_values = np.sort(X_values)

    MF_values = [MF_triangular(X, a, b, c) for X in X_values]

    if negado == -1:
        MF_values = [1 - val for val in MF_values]
        label = f'Triangular Negada (a={a}, b={b}, c={c})'
    elif negado == -2:
        sugeno_s = float(input("Ingresar el valor de s para el complemento de Sugeno: "))
        MF_values = [1 / (1 + sugeno_s * val) for val in MF_values]
        label = f'Triangular Sugeno (a={a}, b={b}, c={c})'
    elif negado == -3:
        yager_w = float(input("Ingresar el valor de w para el complemento de Yager: "))
        MF_values = [min(1, (1 - val ** yager_w) ** (1 / yager_w)) for val in MF_values]
        label = f'Triangular Yager (a={a}, b={b}, c={c})'
    else:
        label = f'Triangular (a={a}, b={b}, c={c})'
        
    calculos.append(MF_values)
    plt.plot(X_values, MF_values, label=label, color=color)

# Función para solicitar los valores de a, b de la función triangular izquierda:
def ltMF_main(auto, A, B, retorno, puntos):
    while True:
        if not auto:
            a = float(input("Ingrese el valor de a: "))
            b = float(input("Ingrese el valor de b: "))
        else:
            a = A
            b = B
            
        if a < b:
            break
        else:
            print("Error: El valor de a debe ser menor que b. Por favor, ingrese los valores nuevamente.")
        
    return[2, a, b, puntos, 0]

# Función para evaluar una MF triangular izquierda:
def MF_triangularIzquierda(X, a, b):
    if X <= a:
        return 1
    elif a < X < b:
        return -(1 / (b - a)) * (X - a) + 1
    else:
        return 0
    
# Función para graficar la MF: 
def plot_MF_triangularIzquierda(a, b, min_universo, max_universo, puntos, color, negado):
    X_values = np.linspace(min_universo, max_universo, puntos)
    X_values = np.concatenate(([a, b], X_values))
    X_values = np.sort(X_values)

    MF_values = [MF_triangularIzquierda(X, a, b) for X in X_values]

    if negado == -1:
        MF_values = [1 - val for val in MF_values]
        label = f'Triangular Negada (a={a}, b={b})'
    elif negado == -2:
        sugeno_s = float(input("Ingresar el valor de s para el complemento de Sugeno: "))
        MF_values = [1 / (1 + sugeno_s * val) for val in MF_values]
        label = f'Triangular Sugeno (a={a}, b={b})'
    elif negado == -3:
        yager_w = float(input("Ingresar el valor de w para el complemento de Yager: "))
        MF_values = [min(1, (1 - val ** yager_w) ** (1 / yager_w)) for val in MF_values]
        label = f'Triangular Yager (a={a}, b={b})'
    else:
        label = f'Triangular (a={a}, b={b})'
    
    calculos.append(MF_values)
    plt.plot(X_values, MF_values, label=label, color=color)

# Función para solicitar los valores de a, b de la función triangular derecha:
def rtMF_main(auto, A, B, retorno, puntos):
    while True:
        if not auto:
            a = float(input("Ingrese el valor de a: "))
            b = float(input("Ingrese el valor de b: "))
        else:
            a = A
            b = B
            
        if a < b:
            break
        else:
            print("Error: El valor de a debe ser menor que b. Por favor, ingrese los valores nuevamente.")

    return[3, a, b, puntos, 0]

# Función para evaluar una MF triangular derecha:
def MF_triangularDerecha(X, a, b):
    if X <= a:
        return 0
    elif a < X < b:
        return (1 / (b - a)) * (X - a)
    else:
        return 1

# Función para graficar la MF:
def plot_MF_triangularDerecha(a, b, min_universo, max_universo, puntos, color, negado):
    X_values = np.linspace(min_universo, max_universo, puntos)
    X_values = np.concatenate(([a, b], X_values))
    X_values = np.sort(X_values)

    MF_values = [MF_triangularDerecha(X, a, b) for X in X_values]
    
    if negado == -1:
        MF_values = [1 - val for val in MF_values]
        label = f'Triangular Negada (a={a}, b={b})'
    elif negado == -2:
        sugeno_s = float(input("Ingresar el valor de s para el complemento de Sugeno: "))
        MF_values = [1 / (1 + sugeno_s * val) for val in MF_values]
        label = f'Triangular Sugeno (a={a}, b={b})'
    elif negado == -3:
        yager_w = float(input("Ingresar el valor de w para el complemento de Yager: "))
        MF_values = [min(1, (1 - val ** yager_w) ** (1 / yager_w)) for val in MF_values]
        label = f'Triangular Yager (a={a}, b={b})'
    else:
        label = f'Triangular (a={a}, b={b})'
    
    calculos.append(MF_values)
    plt.plot(X_values, MF_values, label=label, color=color)

# Función para solicitar los valores de mid, Lsigma y Rsigma de la función gaussiana:
def agMF_main(auto, M, LS, RS, retorno, puntos):
    if not auto:
        mid = float(input("Ingrese el valor del centro: "))
    else:
        mid = M

    while True:
        if not auto:
            Lsigma = float(input("Ingrese el valor de la desviación estándar izquierda (Lsigma): "))
        else:
            Lsigma = LS
            
        if Lsigma > 0:
            break
        else:
            print("Error: El valor de sigma debe ser mayor a cero. Por favor, ingrese el valor nuevamente.")

    while True:
        if not auto:
            Rsigma = float(input("Ingrese el valor de la desviación estándar derecha (Rsigma): "))
        else:
            Rsigma = RS
            
        if Rsigma > 0:
            break
        else:
            print("Error: El valor de sigma debe ser mayor a cero. Por favor, ingrese el valor nuevamente.")
            
    return[4, mid, Lsigma, Rsigma, puntos, 0]

# Función para evaluar una MF gaussiana:
def MF_gaussianaAsimetrica(X, mid, Lsigma, Rsigma):
    if X <= mid:
        return np.exp(-0.5 * ((X - mid) / Lsigma) ** 2)
    else:
        return np.exp(-0.5 * ((X - mid) / Rsigma) ** 2)

# Función para graficar la MF:
def plot_MF_gaussianaAsimetrica(mid, Lsigma, Rsigma, min_universo, max_universo, puntos, color, negado):
    X_values = np.linspace(min_universo, max_universo, puntos)
    MF_values = [MF_gaussianaAsimetrica(X, mid, Lsigma, Rsigma) for X in X_values]
    
    if negado == -1:
        MF_values = [1 - val for val in MF_values]
        label = f'Gaussiana Negada (mid={mid}, Lsigma={Lsigma}, Rsigma={Rsigma})'
    elif negado == -2:
        sugeno_s = float(input("Ingresar el valor de s para el complemento de Sugeno: "))
        MF_values = [1 / (1 + sugeno_s * val) for val in MF_values]
        label = f'Gaussiana Sugeno (mid={mid}, Lsigma={Lsigma}, Rsigma={Rsigma})'
    elif negado == -3:
        yager_w = float(input("Ingresar el valor de w para el complemento de Yager: "))
        MF_values = [min(1, (1 - val ** yager_w) ** (1 / yager_w)) for val in MF_values]
        label = f'Gaussiana Yager (mid={mid}, Lsigma={Lsigma}, Rsigma={Rsigma})'
    else:
        label = f'Gaussiana (mid={mid}, Lsigma={Lsigma}, Rsigma={Rsigma})'

    calculos.append(MF_values)
    plt.plot(X_values, MF_values, label=label, color=color)

# Función para solicitar los valores de mid y sigma de la función gaussiana izquierda:
def lgMF_main(auto, M, S, retorno, puntos):
    if not auto:
        mid = float(input("Ingrese el valor del centro: "))
    else:
        mid = M

    while True:
        if not auto:
            sigma = float(input("Ingrese el valor de la desviación estándar (sigma): "))
        else:
            sigma = S
            
        if sigma > 0:
            break
        else:
            print("Error: El valor de sigma debe ser mayor a cero. Por favor, ingrese el valor nuevamente.")
            
    return[5, mid, sigma, puntos, 0]

# Función para evaluar una MF gaussiana izquierda:
def MF_gaussianaIzquierda(X, mid, sigma):
    if X <= mid:
        return 1
    else:
        return np.exp(-0.5 * ((X - mid) / sigma) ** 2)

# Función para graficar la MF:
def plot_MF_gaussianaIzquierda(mid, sigma, min_universo, max_universo, puntos, color, negado):
    X_values = np.linspace(min_universo, max_universo, puntos)
    X_values = np.concatenate(([mid], X_values))
    X_values = np.sort(X_values)

    MF_values = [MF_gaussianaIzquierda(X, mid, sigma) for X in X_values]
    
    if negado == -1:
        MF_values = [1 - val for val in MF_values]
        label = f'Gaussiana Negada (mid={mid}, sigma={sigma})'
    elif negado == -2:
        sugeno_s = float(input("Ingresar el valor de s para el complemento de Sugeno: "))
        MF_values = [1 / (1 + sugeno_s * val) for val in MF_values]
        label = f'Gaussiana Sugeno (mid={mid}, sigma={sigma})'
    elif negado == -3:
        yager_w = float(input("Ingresar el valor de w para el complemento de Yager: "))
        MF_values = [min(1, (1 - val ** yager_w) ** (1 / yager_w)) for val in MF_values]
        label = f'Gaussiana Yager (mid={mid}, sigma={sigma})'
    else:
        label = f'Gaussiana (mid={mid}, sigma={sigma})'

    calculos.append(MF_values)
    plt.plot(X_values, MF_values, label=label, color=color)

# Función para solicitar los valores de mid y sigma de la función gaussiana derecha:
def rgMF_main(auto, M, S, retorno, puntos):
    if not auto:
        mid = float(input("Ingrese el valor del centro: "))
    else:
        mid = M

    while True:
        if not auto:
            sigma = float(input("Ingrese el valor de la desviación estándar (sigma): "))
        else:
            sigma = S
            
        if sigma > 0:
            break
        else:
            print("Error: El valor de sigma debe ser mayor a cero. Por favor, ingrese el valor nuevamente.")
            
    return[6, mid, sigma, puntos, 0]

# Función para evaluar una MF gaussiana derecha:
def MF_gaussianaDerecha(X, mid, sigma):
    if X > mid:
        return 1
    else:
        return np.exp(-0.5 * ((X - mid) / sigma) ** 2)

# Función para graficar la MF:
def plot_MF_gaussianaDerecha(mid, sigma, min_universo, max_universo, puntos, color, negado):
    X_values = np.linspace(min_universo, max_universo, puntos)
    X_values = np.concatenate(([mid], X_values))
    X_values = np.sort(X_values)

    MF_values = [MF_gaussianaDerecha(X, mid, sigma) for X in X_values]
    
    if negado == -1:
        MF_values = [1 - val for val in MF_values]
        label = f'Gaussiana Negada (mid={mid}, sigma={sigma})'
    elif negado == -2:
        sugeno_s = float(input("Ingresar el valor de s para el complemento de Sugeno: "))
        MF_values = [1 / (1 + sugeno_s * val) for val in MF_values]
        label = f'Gaussiana Sugeno (mid={mid}, sigma={sigma})'
    elif negado == -3:
        yager_w = float(input("Ingresar el valor de w para el complemento de Yager: "))
        MF_values = [min(1, (1 - val ** yager_w) ** (1 / yager_w)) for val in MF_values]
        label = f'Gaussiana Yager (mid={mid}, sigma={sigma})'
    else:
        label = f'Gaussiana (mid={mid}, sigma={sigma})'

    calculos.append(MF_values)
    plt.plot(X_values, MF_values, label=label, color=color)

# Función para solicitar los valores de a, b, c, d de la función trapezoidal:
def tpMF_main(auto, A, B, C, D, retorno, puntos):
    while True:
        if not auto:
            a = float(input("Ingrese el valor de a: "))
            b = float(input("Ingrese el valor de b: "))
            c = float(input("Ingrese el valor de c: "))
            d = float(input("Ingrese el valor de d: "))
        else:
            a = A
            b = B
            c = C
            d = D
            
        if a < b < c < d:
            break
        else:
            print("Error: Los valores deben cumplir con la condición a < b < c < d. Por favor, ingrese los valores nuevamente.")
            
    return[7, a, b, c, d, puntos, 0]

# Función para evaluar una MF trapezoidal:
def MF_trapezoidal(X, a, b, c, d):
    if X <= a:
        return 0
    elif a < X <= b:
        return (X - a) / (b - a)
    elif b < X <= c:
        return 1
    elif c < X < d:
        return (d - X) / (d - c)
    else:
        return 0

# Función para graficar la MF:
def plot_MF_trapezoidal(a, b, c, d, min_universo, max_universo, puntos, color, negado):
    X_values = np.linspace(min_universo, max_universo, puntos)
    MF_values = [MF_trapezoidal(X, a, b, c, d) for X in X_values]
    
    if negado == -1:
        MF_values = [1 - val for val in MF_values]
        label = f'Trapezoidal Negada (a={a}, b={b}, c={c}, d={d})'
    elif negado == -2:
        sugeno_s = float(input("Ingresar el valor de s para el complemento de Sugeno: "))
        MF_values = [1 / (1 + sugeno_s * val) for val in MF_values]
        label = f'Trapezoidal Sugeno (a={a}, b={b}, c={c}, d={d})'
    elif negado == -3:
        yager_w = float(input("Ingresar el valor de w para el complemento de Yager: "))
        MF_values = [min(1, (1 - val ** yager_w) ** (1 / yager_w)) for val in MF_values]
        label = f'Trapezoidal Yager (a={a}, b={b}, c={c}, d={d})'
    else:
        label = f'Trapezoidal (a={a}, b={b}, c={c}, d={d})'

    calculos.append(MF_values)
    plt.plot(X_values, MF_values, label=label, color=color)

# Función para solicitar el valor de a de la función escalón unitario:
def stMF_main(auto, A, retorno, puntos):
    if not auto:
        a = float(input("Ingrese el valor de a: "))
    else:
        a = A
        
    return[8, a, puntos, 0]

# Función para evaluar una MF escalón unitario:
def MF_escalonUnitario(X, a):
    return 1 if X >= a else 0

# Función para graficar la MF:
def plot_MF_escalonUnitario(a, min_universo, max_universo, puntos, color, negado):
    X_values = np.linspace(a - 0.000000001, a + 0.000000001, puntos)
    MF_values = [MF_escalonUnitario(X, a) for X in X_values]
    
    if negado == -1:
        MF_values = [1 - val for val in MF_values]
        label = f'Escalón Negada (a={a})'
    elif negado == -2:
        sugeno_s = float(input("Ingresar el valor de s para el complemento de Sugeno: "))
        MF_values = [1 / (1 + sugeno_s * val) for val in MF_values]
        label = f'Escalón Sugeno (a={a})'
    elif negado == -3:
        yager_w = float(input("Ingresar el valor de w para el complemento de Yager: "))
        MF_values = [min(1, (1 - val ** yager_w) ** (1 / yager_w)) for val in MF_values]
        label = f'Escalón Yager (a={a})'
    else:
        label = f'Escalón (a={a})'

    calculos.append(MF_values)
    plt.plot(X_values, MF_values, label=label, color=color)

# Función para solicitar los valores de c, a, b de la función de Cauchy:
def gbMF_main(auto, C, A, B, retorno, puntos):
    if not auto:
        c = float(input("Ingrese el valor del centro: "))
        a = float(input("Ingrese el valor del ancho (a): "))
        b = float(input("Ingrese el valor del parámetro de forma (b): "))
    else:
        c = C
        a = A
        b = B
    
    return[9, c, a, b, puntos, 0]

# Función para evaluar una MF campana generalizada:
def MF_generalizedBell(X, c, a, b):
    return 1 / (1 + abs((X - c) / a) ** (2 * b))

# Función para graficar la MF:
def plot_MF_generalizedBell(c, a, b, min_universo, max_universo, puntos, color, negado):
    X_values = np.linspace(min_universo, max_universo, puntos)
    MF_values = [MF_generalizedBell(X, c, a, b) for X in X_values]
    
    if negado == -1:
        MF_values = [1 - val for val in MF_values]
        label = f'Cauchy Negada (c={c}, a={a}, b={b})'
    elif negado == -2:
        sugeno_s = float(input("Ingresar el valor de s para el complemento de Sugeno: "))
        MF_values = [1 / (1 + sugeno_s * val) for val in MF_values]
        label = f'Cauchy Sugeno (c={c}, a={a}, b={b})'
    elif negado == -3:
        yager_w = float(input("Ingresar el valor de w para el complemento de Yager: "))
        MF_values = [min(1, (1 - val ** yager_w) ** (1 / yager_w)) for val in MF_values]
        label = f'Cauchy Yager (c={c}, a={a}, b={b})'
    else:
        label = f'Cauchy (c={c}, a={a}, b={b})'

    calculos.append(MF_values)
    plt.plot(X_values, MF_values, label=label, color=color)

# Función para solicitar los valores de c, a, b de la función Izquierda-Derecha:
def lrMF_main(auto, C, A, B, retorno, puntos):
    if not auto:
        c = float(input("Ingrese el valor del centro (c): "))
        alpha = float(input("Ingrese el valor de alpha: "))
        beta = float(input("Ingrese el valor de beta: "))
    else:
        c = C
        alpha = A
        beta = B
        
    return[10, c, alpha, beta, puntos, 0]

# Función para evaluar una MF Izquierda-Derecha (LR):
def MF_leftRight(X, c, alpha, beta):
    if X >= c:
        x1 = (X - c) / beta
        return np.exp(-abs(x1**3))
    else:
        x2 = (c - X) / alpha
        return max(0, np.sqrt(1 - x2**2))

# Función para graficar la MF:
def plot_MF_leftRight(c, alpha, beta, min_universo, max_universo, puntos, color, negado):
    X_values = np.linspace(min_universo, max_universo, puntos)
    MF_values = [MF_leftRight(X, c, alpha, beta) for X in X_values]
    
    if negado == -1:
        MF_values = [1 - val for val in MF_values]
        label = f'LR Negada (alpha={alpha}, beta={beta}, c={c})'
    elif negado == -2:
        sugeno_s = float(input("Ingresar el valor de s para el complemento de Sugeno: "))
        MF_values = [1 / (1 + sugeno_s * val) for val in MF_values]
        label = f'LR Sugeno (alpha={alpha}, beta={beta}, c={c})'
    elif negado == -3:
        yager_w = float(input("Ingresar el valor de w para el complemento de Yager: "))
        MF_values = [min(1, (1 - val ** yager_w) ** (1 / yager_w)) for val in MF_values]
        label = f'LR Yager (alpha={alpha}, beta={beta}, c={c})'
    else:
        label = f'LR (alpha={alpha}, beta={beta}, c={c})'

    calculos.append(MF_values)
    plt.plot(X_values, MF_values, label=label, color=color)

# Función para solicitar los valores de a, c de la función sigmoide:
def sigMF_main(auto, A, C, retorno, puntos):
    if not auto:
        a = float(input("Ingrese el valor de la pendiente (a): "))
        c = float(input("Ingrese el valor del punto de inflexión (c): "))
    else:
        a = A
        c = C
        
    return[11, a, c, puntos, 0]

# Función para evaluar una MF sigmoide:
def MF_sigmoidal(X, a, c):
    return 1 / (1 + np.exp(-a * (X - c)))

# Función para graficar la MF
def plot_MF_sigmoidal(a, c, min_universo, max_universo, puntos, color, negado):
    X_values = np.linspace(min_universo, max_universo, puntos)
    MF_values = [MF_sigmoidal(X, a, c) for X in X_values]
    
    if negado == -1:
        MF_values = [1 - val for val in MF_values]
        label = f'Sigmoide Negada (a={a}, c={c})'
    elif negado == -2:
        sugeno_s = float(input("Ingresar el valor de s para el complemento de Sugeno: "))
        MF_values = [1 / (1 + sugeno_s * val) for val in MF_values]
        label = f'Sigmoide Sugeno (a={a}, c={c})'
    elif negado == -3:
        yager_w = float(input("Ingresar el valor de w para el complemento de Yager: "))
        MF_values = [min(1, (1 - val ** yager_w) ** (1 / yager_w)) for val in MF_values]
        label = f'Sigmoide Yager (a={a}, c={c})'
    else:
        label = f'Sigmoide (a={a}, c={c})'

    calculos.append(MF_values)
    plt.plot(X_values, MF_values, label=label, color=color)

# Función para agregar un vector de unión a las operaciones
def union_main(auto, MF1, MF2, retorno, puntos):
    while True:
        if not auto:
            mf1 = int(input("Seleccione la primera función de membresía: "))
            mf2 = int(input("Seleccione la segunda función de membresía: "))
            print()
        
            if mf1 == mf2:
                print("Selección inválida. Las funciones de membresía deben ser diferentes.")
                print()
            elif 1 <= mf1 <= len(resultados) and 1 <= mf2 <= len(resultados):
                break
            else:
                print("Selección inválida. Inténtelo nuevamente.")
                print()
    
        else:
            mf1 = MF1
            mf2 = MF2
        
    return[100, mf1, mf2, puntos, 0]

# Función para la unión de dos funciones de membresía
def plot_union(MF_values1, MF_values2, min_universo, max_universo, puntos, color, negado):
    X_values = np.linspace(min_universo, max_universo, puntos)
    vector1 = np.array(calculos[MF_values1 - 1])
    vector2 = np.array(calculos[MF_values2 - 1])
    
    if len(vector1) != puntos:
        vector1 = np.interp(X_values, np.linspace(min_universo, max_universo, len(vector1)), vector1)
    if len(vector2) != puntos:
        vector2 = np.interp(X_values, np.linspace(min_universo, max_universo, len(vector2)), vector2)
    
    MF_values = np.maximum(vector1, vector2)
    label = 'Unión'
    plt.plot(X_values, MF_values, label=label, color=color)
    
# Función para agregar un vector de intersección a las operaciones
def interseccion_main(auto, MF1, MF2, retorno, puntos):
    while True:
        if not auto:
            mf1 = int(input("Seleccione la primera función de membresía: "))
            mf2 = int(input("Seleccione la segunda función de membresía: "))
            print()
        
            if mf1 == mf2:
                print("Selección inválida. Las funciones de membresía deben ser diferentes.")
                print()
            elif 1 <= mf1 <= len(resultados) and 1 <= mf2 <= len(resultados):
                break
            else:
                print("Selección inválida. Inténtelo nuevamente.")
                print()
    
        else:
            mf1 = MF1
            mf2 = MF2
        
    return[200, mf1, mf2, puntos, 0]

# Función para la intersección de dos funciones de membresía
def plot_interseccion(MF_values1, MF_values2, min_universo, max_universo, puntos, color, negado):
    X_values = np.linspace(min_universo, max_universo, puntos)
    vector1 = np.array(calculos[MF_values1 - 1])
    vector2 = np.array(calculos[MF_values2 - 1])
    
    if len(vector1) != puntos:
        vector1 = np.interp(X_values, np.linspace(min_universo, max_universo, len(vector1)), vector1)
    if len(vector2) != puntos:
        vector2 = np.interp(X_values, np.linspace(min_universo, max_universo, len(vector2)), vector2)
    
    MF_values = np.minimum(vector1, vector2)
    label = 'Intersección'
    plt.plot(X_values, MF_values, label=label, color=color)

# Función para graficar todas las funciones de membresía una vez hayan sido ingresadas:
def graficar():
    while True:
        min_universo = float(input("Ingrese el valor mínimo del conjunto universo: "))
        max_universo = float(input("Ingrese el valor máximo del conjunto universo: "))
        
        if min_universo < max_universo:
            break
        else:
            print("Error: El valor mínimo del conjunto universo debe ser menor al valor máximo. Por favor, ingrese los valores nuevamente.")
        
    plt.figure(figsize=(10, 6))
    color_index = 0
    
    for operacion in resultados:
        color = colores[color_index % len(colores)]
        if operacion[0] == 1:
            plot_MF_triangular(operacion[1], operacion[2], operacion[3], min_universo, max_universo, operacion[4], color, operacion[5])
        elif operacion[0] == 2:
            plot_MF_triangularIzquierda(operacion[1], operacion[2], min_universo, max_universo, operacion[3], color, operacion[4])
        elif operacion[0] == 3:
            plot_MF_triangularDerecha(operacion[1], operacion[2], min_universo, max_universo, operacion[3], color, operacion[4])
        elif operacion[0] == 4:
            plot_MF_gaussianaAsimetrica(operacion[1], operacion[2], operacion[3], min_universo, max_universo, operacion[4], color, operacion[5])
        elif operacion[0] == 5:
            plot_MF_gaussianaIzquierda(operacion[1], operacion[2], min_universo, max_universo, operacion[3], color, operacion[4])
        elif operacion[0] == 6:
            plot_MF_gaussianaDerecha(operacion[1], operacion[2], min_universo, max_universo, operacion[3], color, operacion[4])
        elif operacion[0] == 7:
            plot_MF_trapezoidal(operacion[1], operacion[2], operacion[3], operacion[4], min_universo, max_universo, operacion[5], color, operacion[6])
        elif operacion[0] == 8:
            plot_MF_escalonUnitario(operacion[1], min_universo, max_universo, operacion[2], color, operacion[3])
        elif operacion[0] == 9:
            plot_MF_generalizedBell(operacion[1], operacion[2], operacion[3], min_universo, max_universo, operacion[4], color, operacion[5])
        elif operacion[0] == 10:
            plot_MF_leftRight(operacion[1], operacion[2], operacion[3], min_universo, max_universo, operacion[4], color, operacion[5])
        elif operacion[0] == 11:
            plot_MF_sigmoidal(operacion[1], operacion[2], min_universo, max_universo, operacion[3], color, operacion[4])
        elif operacion[0] == 100:
            plot_union(operacion[1], operacion[2], min_universo, max_universo, operacion[3], color, operacion[4])
        elif operacion[0] == 200:
            plot_interseccion(operacion[1], operacion[2], min_universo, max_universo, operacion[3], color, operacion[4])

        color_index += 1
        
        if color_index > 10:
            color_index = 0
    
    plt.xlabel('X')
    plt.ylabel('Membership Value')
    plt.title('Membership Functions')
    plt.legend()
    plt.grid(True)
    plt.ylim(-0.1, 1.1)
    plt.xlim(min_universo, max_universo)
    plt.show()

# Función para mostrar el menú principal al usuario:
def menu():
    print()
    print("Funciones de membresía (MF) disponibles:")
    print()
    print("1. MF Triangular.")
    print("2. MF Triangular Izquierda.")
    print("3. MF Triangular Derecha.")
    print("4. MF Gaussiana.")
    print("5. MF Gaussiana Izquierda.")
    print("6. MF Gaussiana Derecha.")
    print("7. MF Trapezoidal.")
    print("8. MF Escalón Unitario.")
    print("9. MF Cauchy.")
    print("10. MF Izquierda-Derecha.")
    print("11. MF Sigmoide.")
    print("12. Salir del programa.")
    print()
    
# Función para mostrar el menú de operaciones al usuario:
def operaciones_menu():
    print()
    print("Operaciones disponibles:")
    print()
    print("1. Graficar funciones de membresía.")
    print("2. Negación de una función de membresía.")
    print("3. Complemento de Sugeno de una función de membresía.")
    print("4. Complemento de Yager de una función de membresía.")
    print("5. Unión de dos funciones de membresía.")
    print("6. Intersección entre dos funciones de membresía.")
    print("7. Salir sin graficar.")
    print()

# Función principal del programa:
def main():
    while True:
        menu()
        opcion = input("Seleccione la MF que desea utilizar: ")
        print()

        if opcion == '1':
            resultados.append(tnMF_main(auto = 0, A = 1, B = 2, C = 3, retorno = 1, puntos = 500))
        elif opcion == '2':
            resultados.append(ltMF_main(auto = 0, A = 1, B = 2, retorno = 1, puntos = 500))
        elif opcion == '3':
            resultados.append(rtMF_main(auto = 0, A = 1, B = 2, retorno = 1, puntos = 500))
        elif opcion == '4':
            resultados.append(agMF_main(auto = 0, M = 5, LS = 1, RS = 1, retorno = 1, puntos = 500))
        elif opcion == '5':
            resultados.append(lgMF_main(auto = 0, M = 5, S = 1, retorno = 1, puntos = 500))
        elif opcion == '6':
            resultados.append(rgMF_main(auto = 0, M = 5, S = 1, retorno = 1, puntos = 500))
        elif opcion == '7':
            resultados.append(tpMF_main(auto = 0, A = 1, B = 2, C = 3, D = 4, retorno = 1, puntos = 500))
        elif opcion == '8':
            resultados.append(stMF_main(auto = 0, A = 1, retorno = 1, puntos = 500))
        elif opcion == '9':
            resultados.append(gbMF_main(auto = 0, C = 5, A = 1, B = 1, retorno = 1, puntos = 500))
        elif opcion == '10':
            resultados.append(lrMF_main(auto = 0, C = 25, A = 10, B = 40, retorno = 1, puntos = 500))
        elif opcion == '11':
            resultados.append(sigMF_main(auto = 0, A = 5, C = 1, retorno = 1, puntos = 500))
        elif opcion == '12':
            print(resultados)
            while True:
                operaciones_menu()
                operacion = input("Seleccione la operación que desea realizar: ")
                print()

                if operacion == '1':
                    graficar()
                    break
                
                elif operacion == '2':
                    if not resultados:
                        print("No hay funciones de membresía para negar.")
                        continue

                    while True:
                        print("Funciones de membresía disponibles para negar:")
                        for i, res in enumerate(resultados, start=1):
                            print(f"{i}. {res}")
                            
                        print()
                        seleccion = int(input("Seleccione la función de membresía que desea negar: "))
                        
                        if 1 <= seleccion <= len(resultados):
                            if resultados[seleccion - 1][-1] == -1:
                                resultados[seleccion - 1][-1] = 0
                            else:
                                resultados[seleccion - 1][-1] = -1
                            print("Función de membresía negada.")
                            break
                        else:
                            print("Selección inválida. Intente nuevamente.")
                            
                elif operacion == '3':
                    if not resultados:
                        print("No hay funciones de membresía para negar.")
                        continue

                    while True:
                        print("Funciones de membresía disponibles para aplicar complemento de Sugeno:")
                        for i, res in enumerate(resultados, start=1):
                            print(f"{i}. {res}")
                        
                        print()
                        seleccion = int(input("Seleccione la función de membresía sobre la cual desea aplicar el complemento: "))
                        
                        if 1 <= seleccion <= len(resultados):
                            if resultados[seleccion - 1][-1] == -2:
                                resultados[seleccion - 1][-1] = 0
                            else:
                                resultados[seleccion - 1][-1] = -2
                            print("Complemento de Sugeno aplicado a la función de membresía.")
                            break
                        else:
                            print("Selección inválida. Intente nuevamente.")
                            
                elif operacion == '4':
                    if not resultados:
                        print("No hay funciones de membresía para negar.")
                        continue

                    while True:
                        print("Funciones de membresía disponibles para aplicar complemento de Yager:")
                        for i, res in enumerate(resultados, start=1):
                            print(f"{i}. {res}")
                        
                        print()
                        seleccion = int(input("Seleccione la función de membresía sobre la cual desea aplicar el complemento: "))
                        
                        if 1 <= seleccion <= len(resultados):
                            if resultados[seleccion - 1][-1] == -3:
                                resultados[seleccion - 1][-1] = 0
                            else:
                                resultados[seleccion - 1][-1] = -3
                            print("Complemento de Yager aplicado a la función de membresía.")
                            break
                        else:
                            print("Selección inválida. Intente nuevamente.")
                            
                elif operacion == '5':
                    if len(resultados) < 2:
                        print("Se requieren al menos dos funciones de membresía para realizar la unión.")
                        continue

                    while True:
                        print("Funciones de membresía disponibles para aplicar la unión:")
                        for i, res in enumerate(resultados, start=1):
                            print(f"{i}. {res}")
                        
                        print()
                        resultados.append(union_main(auto = 0, MF1 = 1, MF2 = 2, retorno = 1, puntos = 500))
                        print("Unión aplicada a las funciones de membresía.")
                        break
                    
                elif operacion == '6':
                    if len(resultados) < 2:
                        print("Se requieren al menos dos funciones de membresía para realizar la intersección.")
                        continue

                    while True:
                        print("Funciones de membresía disponibles para aplicar la intersección:")
                        for i, res in enumerate(resultados, start=1):
                            print(f"{i}. {res}")
                        
                        print()
                        resultados.append(interseccion_main(auto = 0, MF1 = 1, MF2 = 2, retorno = 1, puntos = 500))
                        print("Intersección aplicada a las funciones de membresía.")
                        break

                elif operacion == '7':
                    break
                else:
                    print("Opción no válida. Por favor, seleccione una opción del 1 al 7.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 12.")

main()