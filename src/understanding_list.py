# List
"""
    Las listas nos permiten almacenar informacion en un lugar, 
    la cantidad que tengo: ya sean poco elementos o millones de elementos.
    
    Se recomienda nombrar ima variable del tipo lista en plural.
    En Python los corchetes [] sus elementos van separados por comas.
    Ejemplo:
"""
bicycles= ['trek', 'canondale', 'redline', 'specialized', 'gigant']
print(bicycles)
print(bicycles[0].title())

#Los indicies comienzan en 0 y teminan en n-1, donde n es el numero de elementos
print(bicycles[4].title())

#Accediendo al ultimo elemento
print(bicycles[-1].title()) #ultimo
print(bicycles[-2].title()) #penultimo
print(bicycles[-5].title()) #primer elemento

# Utilizando valores de la lista.
message= "Mi primer bicicleta fue una " +  bicycles[2].title()+ "."
print(message)
message_f= f"Mi primer bicicleta fue una  {bicycles[0].title()}."
print(message_f)

##Agregar elementos a una lista
print("\n")
print("Agregar elementos a una lista")
print(bicycles)

print("Metodo de las listas para agregar elementos: list_name.append(element)")
bicycles.append("Ducatti")
print(bicycles)