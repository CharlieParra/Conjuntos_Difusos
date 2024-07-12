from MF_TriangularIzquierda import ltMF_main
from MF_Triangular import tMF_main
from MF_TriangularDerecha import rtMF_main

def menu():
    print("Funciones de membresía (MF) disponibles:")
    print("1. MF Triangular Izquierda.")
    print("2. MF Triangular.")
    print("3. MF Triangular Derecha.")
    print("4. Salir")

def main():
    while True:
        menu()
        opcion = input("Seleccione la MF que desea utilizar: ")

        if opcion == '1':
            ltMF_main()
        elif opcion == '2':
            tMF_main()
        elif opcion == '3':
            rtMF_main()
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")

main()
