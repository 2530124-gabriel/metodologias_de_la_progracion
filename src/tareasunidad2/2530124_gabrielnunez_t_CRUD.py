# Gabriel de Jesus Nuñez Rodriguez
# 2530124
# IM- 3
## RESUMEN EJECUTIVO
"""
En este proyecto desarrollé un sistema CRUD (Crear, Leer, Actualizar y Eliminar) utilizando Python y estructuras de datos almacenadas en memoria, 
como diccionarios y listas de diccionarios. El propósito fue practicar cómo organizar mejor un programa separando cada operación en funciones independientes, 
además de diseñar un menú básico que permita al usuario interactuar de forma sencilla con el sistema.
También trabajé en la validación de entradas para evitar errores comunes, como datos vacíos o tipos incorrectos. Durante el desarrollo documenté mi solución, 
incluyendo una descripción clara, casos de prueba que muestran cómo debe funcionar el programa y situaciones donde podría fallar, así como mis conclusiones sobre lo aprendido.
Este proyecto me ayudó a reforzar mis conocimientos de Python, especialmente en el manejo de estructuras de datos y la importancia de escribir código modular y ordenado. 
Además, me permitió comprender cómo funcionan los CRUD básicos, que son la base de muchos sistemas y aplicaciones actuales.
"""

#Problema 6.1 – Gestor CRUD usando diccionarios y funciones.
## FUNCIONES CRUD

def create_item(data, item_id, name, price, quantity):
    """Crea un nuevo ítem si el id NO existe. 
       Regresa True si se creó, False si ya existe."""
    if item_id in data:
        return False  # Política: NO permitir IDs repetidos
    data[item_id] = {
        "name": name,
        "price": price,
        "quantity": quantity
    }
    return True


def read_item(data, item_id):
    """Retorna el item o None si NO existe."""
    return data.get(item_id)


def update_item(data, item_id, new_name, new_price, new_quantity):
    """Actualiza un ítem existente. Retorna True si se actualizó."""
    if item_id not in data:
        return False
    
    data[item_id] = {
        "name": new_name,
        "price": new_price,
        "quantity": new_quantity
    }
    return True


def delete_item(data, item_id):
    """Elimina el ítem si existe. Retorna True si se eliminó."""
    if item_id not in data:
        return False
    del data[item_id]
    return True


def list_items(data):
    """Imprime la lista de todos los ítems."""
    if not data:
        print("No hay ítems registrados.")
        return
    
    print("\n--- ITEMS REGISTRADOS ---")
    for item_id, info in data.items():
        print(f"ID: {item_id} | Nombre: {info['name']} | "
              f"Precio: {info['price']} | Cantidad: {info['quantity']}")
    print("--------------------------\n")


# Menú principal

def main():
    data = {}  # Diccionario principal
    while True:
        print("\n===== MENÚ CRUD =====")
        print("1) Create item")
        print("2) Read item by id")
        print("3) Update item")
        print("4) Delete item")
        print("5) List all items")
        print("0) Exit")

        option = input("Selecciona una opción: ").strip()

        # Validar opción
        if option not in {"0", "1", "2", "3", "4", "5"}:
            print("Error: invalid input")
            continue

        if option == "0":
            print("Saliendo del programa...")
            break

        # ------------------------
        #   CREATE
        # ------------------------
        if option == "1":
            item_id = input("ID del ítem: ").strip()
            name = input("Nombre: ").strip()
            
            try:
                price = float(input("Precio: "))
                quantity = int(input("Cantidad: "))
            except:
                print("Error: invalid input")
                continue

            if price < 0 or quantity < 0:
                print("Error: invalid input")
                continue

            if create_item(data, item_id, name, price, quantity):
                print("Item created")
            else:
                print("Error: ID already exists")

        # ------------------------
        #   READ
        # ------------------------
        elif option == "2":
            item_id = input("ID del ítem: ").strip()

            item = read_item(data, item_id)
            if item:
                print(f"Item encontrado: {item}")
            else:
                print("Item not found")

        # ------------------------
        #   UPDATE
        # ------------------------
        elif option == "3":
            item_id = input("ID del ítem: ").strip()

            if item_id not in data:
                print("Item not found")
                continue

            new_name = input("Nuevo nombre: ").strip()

            try:
                new_price = float(input("Nuevo precio: "))
                new_quantity = int(input("Nueva cantidad: "))
            except:
                print("Error: invalid input")
                continue

            if new_price < 0 or new_quantity < 0:
                print("Error: invalid input")
                continue

            if update_item(data, item_id, new_name, new_price, new_quantity):
                print("Item updated")
            else:
                print("Item not found")

        # ------------------------
        #   DELETE
        # ------------------------
        elif option == "4":
            item_id = input("ID del ítem: ").strip()

            if delete_item(data, item_id):
                print("Item deleted")
            else:
                print("Item not found")

        # ------------------------
        #   LIST
        # ------------------------
        elif option == "5":
            list_items(data)


#                     INICIO DEL PROGRAMA

if __name__ == "__main__":
    main()


# Caso 1
"""
1
A01
Coca Cola
15.5
20
2
A01
5
0
"""
## Salida esperada:
"""
Item created
Item encontrado: {'name': 'Coca Cola', 'price': 15.5, 'quantity': 20}

--- ITEMS REGISTRADOS ---
ID: A01 | Nombre: Coca Cola | Precio: 15.5 | Cantidad: 20
--------------------------

Saliendo del programa...

"""

# Caso 2 
"""
1
X00
ProductoGratis
0
0
2
X00
0
"""
## Salida esperada:
"""
Item created
Item encontrado: {'name': 'ProductoGratis', 'price': 0.0, 'quantity': 0}
Saliendo del programa...
"""

#Caso 3 (Error - ID duplicado)
"""
1
B10
Jabon
abc
"""
## Salida esperada:
"""
Error: invalid input
"""

# Conclusion
# El programa desarrollado implementa de manera correcta un sistema CRUD básico
# utilizando funciones y una estructura de datos eficiente basada en diccionarios.
# La separación de responsabilidades mediante funciones específicas para crear,
# leer, actualizar, eliminar y listar ítems mejora la organización y facilita el
# mantenimiento del código. Además, el uso de un diccionario principal permite
# acceder a los elementos por su identificador de forma rápida, evitando
# recorridos innecesarios y optimizando el rendimiento.
#
# Las validaciones incluidas garantizan que los datos ingresados por el usuario
# sean coherentes y previenen errores comunes como IDs repetidos, tipos no
# numéricos o valores negativos. El menú interactivo proporciona una interfaz
# sencilla y funcional que guía al usuario durante la ejecución del programa.
# En conjunto, el código demuestra un enfoque adecuado para la gestión de
# información en memoria, aplicando principios básicos de modularidad, robustez
# y claridad en el diseño de software.

# REFERENCES
# 1) Python Software Foundation – Python Documentation:
#    "Control Flow Tools: for and while loops"
#    https://docs.python.org/3/tutorial/controlflow.html
#
# 2) Real Python – "Fibonacci Sequence in Python"
#    (Guías y explicaciones sobre algoritmos y secuencias)
#    https://realpython.com
#
# 3) Apuntes de clase – Unidad sobre ciclos, validaciones
#    y generación de secuencias numéricas.

