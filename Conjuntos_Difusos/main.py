import matplotlib.pyplot as plt

from MF_TriangularIzquierda import plot_MF_triangularIzquierda
from MF_Triangular import plot_MF_triangular
from MF_TriangularDerecha import plot_MF_triangularDerecha
from MF_GaussianaIzquierda import plot_MF_gaussianaIzquierda
from MF_Gaussiana import plot_MF_gaussianaAsimetrica
from MF_GaussianaDerecha import plot_MF_gaussianaDerecha
from MF_Trapezoidal import plot_MF_trapezoidal
from MF_EscalonUnitario import plot_MF_escalonUnitario
from MF_CampanaGeneralizada import plot_MF_generalizedBell
from MF_IzquierdaDerecha import plot_MF_leftRight
from MF_Sigmoidea import plot_MF_sigmoidal

resultados = []
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

    return [1, a, b, c, puntos]

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
        
    return[2, a, b, puntos]

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

    return[3, a, b, puntos]

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
            
    return[4, mid, Lsigma, Rsigma, puntos]

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
            
    return[5, mid, sigma, puntos]

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
            
    return[6, mid, sigma, puntos]

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
            
    return[7, a, b, c, d, puntos]

# Función para solicitar el valor de a y el rango del conjunto universo:
def stMF_main(auto, A, retorno, puntos):
    if not auto:
        a = float(input("Ingrese el valor de a: "))
    else:
        a = A
        
    return[8, a, puntos]

# Función para solicitar los valores de c, a, b y el rango del conjunto universo:
def gbMF_main(auto, C, A, B, retorno, puntos):
    if not auto:
        c = float(input("Ingrese el valor del centro: "))
        a = float(input("Ingrese el valor del ancho (a): "))
        b = float(input("Ingrese el valor del parámetro de forma (b): "))
    else:
        c = C
        a = A
        b = B
    
    return[9, c, a, b, puntos]

# Función para solicitar los valores de c, a, b y el rango del conjunto universo:
def lrMF_main(auto, C, A, B, retorno, puntos):
    if not auto:
        c = float(input("Ingrese el valor del centro (c): "))
        alpha = float(input("Ingrese el valor de alpha: "))
        beta = float(input("Ingrese el valor de beta: "))
    else:
        c = C
        alpha = A
        beta = B
        
    return[10, c, alpha, beta, puntos]

# Función para solicitar los valores de a, c y el rango del conjunto universo
def sigMF_main(auto, A, C, retorno, puntos):
    if not auto:
        a = float(input("Ingrese el valor de la pendiente (a): "))
        c = float(input("Ingrese el valor del punto de inflexión (c): "))
    else:
        a = A
        c = C
        
    return[11, a, c, puntos]

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
            plot_MF_triangular(operacion[1], operacion[2], operacion[3], min_universo, max_universo, operacion[4], color)
        elif operacion[0] == 2:
            plot_MF_triangularIzquierda(operacion[1], operacion[2], min_universo, max_universo, operacion[3], color)
        elif operacion[0] == 3:
            plot_MF_triangularDerecha(operacion[1], operacion[2], min_universo, max_universo, operacion[3], color)
        elif operacion[0] == 4:
            plot_MF_gaussianaAsimetrica(operacion[1], operacion[2], operacion[3], min_universo, max_universo, operacion[4], color)
        elif operacion[0] == 5:
            plot_MF_gaussianaIzquierda(operacion[1], operacion[2], min_universo, max_universo, operacion[3], color)
        elif operacion[0] == 6:
            plot_MF_gaussianaDerecha(operacion[1], operacion[2], min_universo, max_universo, operacion[3], color)
        elif operacion[0] == 7:
            plot_MF_trapezoidal(operacion[1], operacion[2], operacion[3], operacion[4], min_universo, max_universo, operacion[5], color)
        elif operacion[0] == 8:
            plot_MF_escalonUnitario(operacion[1], min_universo, max_universo, operacion[2], color)
        elif operacion[0] == 9:
            plot_MF_generalizedBell(operacion[1], operacion[2], operacion[3], min_universo, max_universo, operacion[4], color)
        elif operacion[0] == 10:
            plot_MF_leftRight(operacion[1], operacion[2], operacion[3], min_universo, max_universo, operacion[4], color)
        elif operacion[0] == 11:
            plot_MF_sigmoidal(operacion[1], operacion[2], min_universo, max_universo, operacion[3], color)

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
    print("11. MF Sigmoidea.")
    print("12. Salir del programa.")
    print()
    
# Función para mostrar el menú secundario al usuario:
def menu2():
    print()
    print("¿Desea realizar alguna operación con las funciones añadidas o graficarlas directamente?")
    print()
    print("1. Ingresar al menú de operaciones.")
    print("2. Graficar y salir.")
    print("3. Regresar al menú de funciones de membresía.")
    print()
    
# Función para mostrar el menú de operaciones al usuario:
def operaciones():
    print("Operaciones disponibles:")
    print("1. Negación.")
    print("2. Unión.")
    print("3. Intersección.")

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
            if resultados:
                print(resultados)
                menu2()
                opcion = input("Seleccione la opción que desea ejecutar: ")
                print()
                
                if opcion == '1':
                    operaciones()
                    opcion = input("Seleccione la operación que desea realizar: ")
                    print()
                    
                elif opcion == '2':
                    graficar()
                elif opcion == '3':
                    main()
                else:
                    print("Opción no válida. Por favor, seleccione una opción del 1 al 3.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 12.")

# Ejecución del programa:
main()
