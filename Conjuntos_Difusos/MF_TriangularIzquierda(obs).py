# Función para evaluar una MF triangular izquierda:
# X = Punto de evaluación.
# a = Vértice izquierdo de la función triangular.
# b = Vértice derecho de la función triangular.
# min_universo = Valor mínimo del conjunto universo.
# max_universo = Valor máximo del conjunto universo.

#from plot_functions import plot_MF_triangularIzquierda

def MF_triangularIzquierda(X, a, b):
    if X <= a:
        return 1
    elif a < X < b:
        return -(1 / (b - a)) * (X - a) + 1
    else:
        return 0



    #resultado=plot_MF_triangularIzquierda(a, b, min_universo, max_universo)
    #if(retorname):
        #return (axax)
    

    
    return ([X_values, MF_values ])