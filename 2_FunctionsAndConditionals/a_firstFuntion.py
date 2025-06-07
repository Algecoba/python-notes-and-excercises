#La sintaxis de una función es la siguiente:
"""
 def nombre_de_la_funcion(parametros):

    Documentación de la función.
    # Cuerpo de la función
    return resultado    
"""

# Definición de una función

def mean(lista):
    """
    Esta función calcula la media de una lista de números.
    """
    the_mean = sum(lista) / len(lista)
    return the_mean

# Llamada a la función
print(mean([1, 2, 3, 4, 5]))  # Imprime: 3.0

#Square Area (E) Define a function that calculates the area of a square
def square_area(side_length):
    """
    Esta función calcula el área de un cuadrado dado su lado.
    """
    area = side_length ** 2
    return area