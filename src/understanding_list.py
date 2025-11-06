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

"""
    # Listas A-105
    Agrega elementos a una lista 
    append(): Agrega un elemento al final de la lista. 
"""

print("\n---- Agregar elementos a una lista metodo append()---")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles) # Salida: ['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')
print(motorcycles)# Salida ['honda', 'yamaha', 'suzuki']

"""
    Agregar elementos a una lista en una posicion especifica
        - insert(): insertar un elemento en una posicion especifica
"""

print("\n---- Insertar elementos en una posición específica (insert) ---")
# Usamos la lista de ejemplo de motocicletas
motorcycles = ['honda', 'yamaha', 'suzuki']
print("Antes:", motorcycles)

# insert(posicion, elemento) inserta el elemento antes del índice dado
# insertar al inicio (índice 0)
motorcycles.insert(0, 'ducati')
print("Insertar al inicio (index 0):", motorcycles)

# insertar en una posición intermedia (por ejemplo, índice 2)
motorcycles.insert(2, 'kawasaki')
print("Insertar en índice 2:", motorcycles)

# si el índice es mayor que la longitud, el elemento se añade al final
motorcycles.insert(100, 'bmw')
print("Insertar con índice grande (se añade al final):", motorcycles)

# ejemplos rápidos: insert puede usar índices negativos (cuenta desde el final)
motorcycles.insert(-1, 'vespa')
print("Insertar con índice -1 (antes del último):", motorcycles)



"""
    Eliminar elementos de una lista y usar el valor eliminado
        -pop (): Eliminar y devuelve el ultimo elemnto de la lista
"""

print("\n---- Eliminar elementos y usar el valor eliminado (pop) ---")
# pop() elimina y devuelve el último elemento si no se pasa índice
cars = ['toyota', 'ford', 'chevrolet', 'nissan']
print("Lista inicial:", cars)
last_car = cars.pop()
print("Elemento eliminado con pop() sin índice:", last_car)
print("Lista después de pop():", cars)

# pop(index) elimina y devuelve el elemento en la posición dada
second_car = cars.pop(1)
print("Elemento eliminado con pop(1):", second_car)
print("Lista después de pop(1):", cars)

# usar pop para procesar elementos uno por uno
print("Procesando y eliminando elementos con pop():")
while cars:
    item = cars.pop()
    print("  Procesado:", item)

# Ejemplo de error manejado: pop en lista vacía lanza IndexError
empty = []
try:
    empty.pop()
except IndexError as e:
    print("Intentar pop() en lista vacía produce:", type(e).__name__)


"""
    Eliminar un elemento especifico de una lista por su valor
        - remove(): Elimina la primera ocurrencia del valor especificado
"""


"""
    # Listas A-105
    Organizar una lista permanentemente
        -sort(): Ordena la lista en orden alfabetico.
"""

print("\n---- Ordenar listas permanentemente con sort() y temporalmente con sorted() ---")
# sort() modifica la lista en sitio (permanente)
cities = ['london', 'paris', 'tokyo', 'madrid', 'sydney']
print("cities original:", cities)
cities.sort()
print("cities después de sort():", cities)

# sort(reverse=True) ordena en orden inverso
cities.sort(reverse=True)
print("cities después de sort(reverse=True):", cities)

# sorted(lista) devuelve una nueva lista ordenada sin modificar la original
numbers = [3, 1, 4, 1, 5, 9]
print("numbers original:", numbers)
sorted_numbers = sorted(numbers)
print("sorted(numbers) devuelve:", sorted_numbers)
print("numbers permanece igual:", numbers)

# sorted puede recibir reverse=True también
print("sorted(numbers, reverse=True):", sorted(numbers, reverse=True))

# ordenar con criterio: usar key (por ejemplo, longitud de palabra)
words = ['banana', 'pie', 'Washington', 'book']
print("words original:", words)
words.sort(key=len)
print("words ordenadas por longitud (sort(key=len)):", words)


# Ejemplos aplicados a la lista motorcycles para mantener consistencia
print("\n---- Ordenar la lista 'motorcycles' (sort vs sorted) ---")
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati', 'kawasaki', 'bmw']
print("motorcycles original:", motorcycles)

# Orden permanente
motorcycles.sort()
print("motorcycles después de sort():", motorcycles)

# Orden permanente inverso
motorcycles.sort(reverse=True)
print("motorcycles después de sort(reverse=True):", motorcycles)

# Orden temporal con sorted() (devuelve nueva lista)
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati', 'kawasaki', 'bmw']
print("sorted(motorcycles):", sorted(motorcycles))
print("motorcycles sigue igual:", motorcycles)

# Ordenar por longitud de nombre
motorcycles.sort(key=len)
print("motorcycles ordenadas por longitud (sort(key=len)):", motorcycles)


"""
Ejemplo: 
"""
students = ["jesus", "josue", "andrix", "miguel" ,"jen", "africa"]
print(students)
desired_students = input("Ingrese el nombre del estudiante que desea eliminar: ")
students.remove(desired_students.strip().lower())
print(students)
print("Tu has eliminado a ", desired_students)
students.reverse()
print(students)

print(len(students))

cars = ["kia", "ford", "tesla", "volvo", "chevrolet"]
cars.sort()
print(cars)
print(sorted(cars))
sorted_list= sorted(cars)
print("lista original", cars)