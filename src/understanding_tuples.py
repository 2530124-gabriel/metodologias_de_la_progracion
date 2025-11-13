# Tuples
"""
    Las tuplas son listas de elementos que no cambian 
    de tamaño. Las tuplas son INMUTABLES.

    Se utilizan los () para definir una tupla.
"""
rectangle= (200,50) # (largo, ancho)
print(rectangle[0])
print(rectangle[1])

#for measure in rectangle_measurement:
   # print(measure)

# print(dir(rectangle_measurement)) # built in dir

#Regresando a las listas
cars= ["bwm", "porche", "masda"]
print(cars)
cars[0]= "bmw"
cars[1]= "porshe"
cars[2]= "Mazda"    
print(cars)


"""
    No podemos modificar una tupla directamente
    lo que si podemos hacer es cambiar la asignacion 
    a una variable que almacena una tupla.
"""