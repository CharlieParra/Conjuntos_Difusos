from MF_TriangularIzquierda import ltMF_main
from MF_Triangular import tnMF_main
from MF_TriangularDerecha import rtMF_main
from MF_GaussianaIzquierda import lgMF_main
from MF_Gaussiana import agMF_main
from MF_GaussianaDerecha import rgMF_main
from MF_Trapezoidal import tpMF_main
from MF_EscalonUnitario import stMF_main
from MF_CampanaGeneralizada import gbMF_main
from MF_IzquierdaDerecha import lrMF_main

def menu():
    print("Funciones de membresía (MF) disponibles:")
    print("1. MF Triangular Izquierda.")
    print("2. MF Triangular.")
    print("3. MF Triangular Derecha.")
    print("4. MF Gaussiana Izquierda.")
    print("5. MF Gaussiana.")
    print("6. MF Gaussiana Derecha.")
    print("7. MF Trapezoidal.")
    print("8. MF Escalón Unitario.")
    print("9. MF Campana generalizada.")
    print("10. MF Izquierda-Derecha.")
    print("11. Salir")

def main():
    while True:
        menu()
        opcion = input("Seleccione la MF que desea utilizar: ")

        if opcion == '1':
            ltMF_main()
        elif opcion == '2':
            tnMF_main()
        elif opcion == '3':
            rtMF_main()
        elif opcion == '4':
            lgMF_main()
        elif opcion == '5':
            agMF_main()
        elif opcion == '6':
            rgMF_main()
        elif opcion == '7':
            tpMF_main()
        elif opcion == '8':
            stMF_main()
        elif opcion == '9':
            gbMF_main()
        elif opcion == '10':
            lrMF_main()
        elif opcion == '11':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 11.")

main()
