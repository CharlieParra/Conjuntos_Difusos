from MF_Triangular3D import tnMF_3D_main
from MF_Trapezoidal3D import trapezoidalMF_3D_main
from MF_Gaussiana3D import gaussianMF_3D_main
from MF_CampanaGeneralizada3D import cauchyMF_3D_main
from MF_IzquierdaDerecha3D import leftRightMF_3D_main
from MF_Sigmoidea3D import sigmoidMF_3D_main

def menu():
    print("Funciones de membresía (MF) tridimensionales disponibles:")
    print("1. MF Triangular.")
    print("2. MF Trapezoidal.")
    print("3. MF Gaussiana.")
    print("4. MF Campana generalizada.")
    print("5. MF Izquierda-Derecha.")
    print("6. MF Sigmoidea.")
    print("7. Salir")
    
def main():
    while True:
        menu()
        opcion = input("Seleccione la MF que desea utilizar: ")

        if opcion == '1':
            tnMF_3D_main()
        elif opcion == '2':
            trapezoidalMF_3D_main()
        elif opcion == '3':
            gaussianMF_3D_main()
        elif opcion == '4':
            cauchyMF_3D_main()
        elif opcion == '5':
            leftRightMF_3D_main()
        elif opcion == '6':
            sigmoidMF_3D_main()
        elif opcion == '7':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del 1 al 7.")

main()