# Gabriel de Jesus Nuñez Rodriguez
# 2530124
# IM- 3
## Resuemen ejecutivo: 
## En este archivo se resuelven seis problemas relacionados con estructuras de datos en Python, incluyendo listas, tuplas y diccionarios. 
## Cada problema aborda una tarea específica, desde la gestión de listas de compras hasta la validación de correos electrónicos y el manejo de calificaciones estudiantiles. 
## Se implementan validaciones para asegurar la integridad de los datos y se proporcionan salidas claras para cada operación realizada.
# Problem 1: Shopping list basics (list operations)
print("Problem 1: Shopping list basics (list operations)")
# Entradas de ejemplo (pueden venir de input())
shopping_list = ["manzanas", "bananas", "cerezas", "dátiles", "higos"]
new_item = "kiwi"
search_item = "cerezas"
# Validaciones
if shopping_list == "":
    item_list = []
    print("La lista de compras esta vacia")
    # Agregar nuevo item
else:
    item_list = [shopping_list.strip() for item_list in shopping_list.split(",")]
    if new_item == "":
        ValueError("El nuevo item no puede estar vacio")
    if search_item == "":
        ValueError("El item a buscar no puede estar vacio")
        # Agregar nuevo item
    item_list.append(new_item.strip())
    len_list = len(item_list)
    is_in_item = search_item.strip() in item_list

    # Salidas
    print("Lista de compras:", item_list)
    print("Numero de items en la lista:", len_list)
    print("El item buscado esta en la lista:", is_in_item)
"""
Caso 1 (funcione)
Entrada: new_item = "kiwi", search_item = "cerezas"
Salida esperada:
Lista: ["manzanas","bananas","cerezas","dátiles","higos","kiwi"]
Número de ítems: 6
is_in_item: True
Por qué: flujo normal.

Caso 2 (apunto de romperse)
Entrada: new_item = " MANGO ", search_item = "BANANAS" (mayúsculas/espacios)
Salida esperada:
Lista (tras .strip() y normalizar a minúsculas si se implementa): ["manzanas","bananas","cerezas","dátiles","higos","mango"]
is_in_item: True (si el código normaliza mayúsc/minúsc).
Por qué: borde por espacios y mayúsculas — falla si no se limpian/casefold.

Caso 3 (código roto)
Entrada: shopping_list = "" (lista como cadena), new_item = "", search_item = ""
Salida esperada/efecto:
Debe lanzar/mostrar error o crear lista vacía. Si el código intenta shopping_list.split(",") sin validar, puede comportarse mal o crear [""].
Resultado erróneo típico: lista [""] y añadir "" → conteo incorrecto; o excepción si se espera lista.
Por qué: tipo incorrecto o strings vacíos sin validación rompen el flujo.
"""

# Problem 2: Points and distances with tuples
print("\nProblem 2: Points and distances with tuples")
x1, y1 = float(2, 3)
x2, y2 = float(5, 7)
point1 = (x1, y1)
point2 = (x2, y2)
distances = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
point_mid = ((x1 + x2) / 2, (y1 + y2) / 2)
# Salidas
print("Punto 1:", point1)
print("Punto 2:", point2)
print("Distancia entre puntos:", distances)
print("Punto medio:", point_mid)
aso 1 (funcione)
"""
Caso 1 (funcione)
Entrada: point1=(2,3), point2=(5,7)
Salida esperada:
Distancia: 5.0
Punto medio: (3.5, 5.0)
Por qué: cálculo normal con números.

Caso 2 (apunto de romperse)
Entrada: point1=("2","3"), point2=("5","7") (números como strings)
Salida esperada:
Si el código convierte con float(): funciona → distancia 5.0.
Si no hay conversión, operaciones aritméticas lanzan TypeError.
Por qué: borderline por tipos; aceptable si hay casting robusto.

Caso 3 (código roto)
Entrada: point1=(2,) (tupla incompleta), point2=(5,7)
Salida esperada/efecto:
Error como ValueError o IndexError al intentar desempaquetar x1,y1 = point1.
Por qué: tupla con tamaño incorrecto rompe desempaquetado.
"""
# Problem 3: Product catalog with dictionary
print("\nProblem 3: Product catalog with dictionary")
product_name = ["manzana", "banana", "cereza"]
quantity = int[10, 20, 15]

# ENTRADA DEL USUARIO
product_cliente = "banana"
quantity_cliente = 3
# Validaciones
product_cliente = product_cliente.strip().lower()
if product_name == "" or quantity  <= 0:
    print("Catalogo de productos vacio")
    # Verificar si el producto existe
if product_cliente in product_name:
    unit_price = product_name(quantity)
    total_price = unit_price * quantity_cliente

    print("Unit price " unit_price)
    print("Quantity:", quantity_cliente)
    print("Total price:", total_price)
else:
    ValueError("Producto no encontrado en el catalogo")
Forma correcta esperada: catalog = {"manzana":10, "banana":20, "cereza":15}
"""
Caso 1 (funcione)
Entrada: product_cliente="banana", quantity_cliente=3
Salida esperada: unit_price=20, total_price=60
Por qué: clave existe y cantidad válida.

Caso 2 (apunto de romperse)
Entrada: product_cliente=" banana " (espacios), quantity_cliente="3" (string)
Salida esperada:
Si hay .strip() y conversión a int: funciona → total 60.
Si no hay conversión: multiplicar string por int falla o produce comportamiento extraño.
Por qué: entradas en tipo/formatos diferentes — borde si no normalizas.

Caso 3 (código roto)
Entrada: product_cliente="pera", quantity_cliente=2 (producto no existe)
Salida esperada/efecto:
Debe producir mensaje de "Producto no encontrado" o lanzar KeyError si intentas acceder sin comprobar.
Por qué: falta de existencia en catálogo rompe acceso directo.
"""

# Problem 4: Student grades with dict and list
print("\nProblem 4: Student grades with dict and list")

# 1) Diccionario inicial con al menos 3 estudiantes
students = {
    "Gabriel": [85, 90, 78],
    "Maria": [92, 88, 95],
    "Luis": [76, 81, 79]
}

# 2) Leer nombre del estudiante (ejemplo fijo, pero puede venir de input)
student_name = ("Gabriel").strip()


# Validaciones
if student_name == "":
    print("Error: student name cannot be empty")

elif student_name in students:

    grades_list = students[student_name]

    # Validar que la lista no esté vacía
    if len(grades_list) == 0:
        print("Error: grades list is empty")
    else:
        # 3) Calcular promedio
        average = sum(grades_list) / len(grades_list)

        # 4) Determinar si aprobó
        is_passed = average >= 70.0

        # Salidas solicitadas
        print("Grades:", grades_list)
        print("Average:", average)
        print("Passed:", str(is_passed).lower())

else:
    print("Error: student not found")
"""
Caso 1 (funcione)
Entrada: student_name="Gabriel"
Salida esperada: grades=[85,90,78], average=84.333..., passed=True
Por qué: estudiante existe y lista de notas válida.

Caso 2 (apunto de romperse)
Entrada: student_name="Maria", pero students["Maria"] = [] (lista vacía)
Salida esperada:
Código correcto devuelve error/control: "grades list is empty" o evita división por cero.
Si no hay validación → ZeroDivisionError al calcular promedio.
Por qué: lista vacía produce división por cero.

Caso 3 (código roto)
Entrada: student_name="" (cadena vacía) o student_name="Pedro" no en dict
Salida esperada/efecto:
Debe mostrar "Error: student not found" o "student name cannot be empty".
Si no valida, KeyError al acceder students[student_name].
Por qué: entrada no válida/ausente rompe el acceso.
"""

# Problem 5: Word frequency counter (list + dict)
print("\nProblem 5: Word frequency counter (list + dict)")

print("\nProblem 5: Word frequency counter")

# 1) Entrada (ejemplo, puede venir de input())
sentence = "Hola, hola mundo! Este mundo es grande."


# Validaciones

sentence = sentence.strip()

if sentence == "":
    print("Error: sentence cannot be empty")

else:
    # DECISIÓN: eliminar puntuación simple (.,!?) usando replace()
    # Esto facilita que palabras como "hola," y "hola" cuenten igual.
    for p in [",", ".", "!", "?"]:
        sentence = sentence.replace(p, "")

    # 2) Convertir a minúsculas y separar
    words_list = sentence.lower().split()

    if len(words_list) == 0:
        print("Error: words list is empty")
    else:
        # 3) Construir diccionario de frecuencias
        freq_dict = {}

        for word in words_list:
            if word in freq_dict:
                freq_dict[word] += 1
            else:
                freq_dict[word] = 1

        # 4) Encontrar la palabra más frecuente
        most_common_word = None
        max_freq = 0

        for word, freq in freq_dict.items():
            if freq > max_freq:
                max_freq = freq
                most_common_word = word

       
        # Salidas requeridas
        
        print("Words list:", words_list)
        print("Frequencies:", freq_dict)
        print("Most common word:", most_common_word)
"""
Caso 1 (funcione)
Entrada: sentence = "Hola, hola mundo! Este mundo es grande."
Salida esperada:
words_list = ["hola","hola","mundo","este","mundo","es","grande"]
freq_dict = {"hola":2,"mundo":2,"este":1,"es":1,"grande":1}
most_common_word -> "hola" o "mundo" (si empate, comportamiento definido por implementación).
Por qué: puntuación removida y normalización a minúsculas.

Caso 2 (apunto de romperse)
Entrada: sentence = " " (solo espacios)
Salida esperada:
Si hay .strip() y chequeo → “Error: sentence cannot be empty”.
Si no hay chequeo → words_list = [] y más tarde puede fallar al buscar most_common_word.
Por qué: cadena vacía tras strip es borde.

Caso 3 (código roto)
Entrada: sentence = None (no string)
Salida esperada/efecto:
Lanza AttributeError al hacer .strip() si no se valida el tipo.
Por qué: tipo incorrecto rompe el flujo.
"""
# Problem 6: Simple contact book (dictionary CRUD)
print("\nProblem 6: Simple contact book (dictionary CRUD)")

print("\nProblem 6: Mini contact book")

# 1) Diccionario inicial con algunos contactos
contacts = {
    "Alice": "1234567890",
    "Bob": "5552223344",
    "Carlos": "9988776655"
}

# Entradas de ejemplo (pueden venir de input())
action_text = "ADD"
name = "Diana"
phone = "4441112233"


# Validaciones iniciales

action = action_text.strip().upper()

if action not in ["ADD", "SEARCH", "DELETE"]:
    print("Error: invalid action")
else:

    # Validar name
    name = name.strip()
    if name == "":
        print("Error: name cannot be empty")

    else:
        
        # Acción ADD
       
        if action == "ADD":
            phone = phone.strip()
            if phone == "":
                print("Error: phone cannot be empty")
            else:
                contacts[name] = phone
                print("Contact saved:", name + ",", phone)

      
        # Acción SEARCH
       
        elif action == "SEARCH":
            if name in contacts:
                print("Phone:", contacts[name])
            else:
                print("Error: contact not found")

      
        # Acción DELETE
     
        elif action == "DELETE":
            if name in contacts:
                contacts.pop(name)
                print("Contact deleted:", name)
            else:
                print("Error: contact not found")

contacts = {"Alice":"1234567890","Bob":"5552223344","Carlos":"9988776655"}
"""
Caso 1 (funcione)
Entrada: action="ADD", name="Diana", phone="4441112233"
Salida esperada: Contact saved: Diana, 4441112233
Por qué: acción válida y campos no vacíos.

Caso 2 (apunto de romperse)
Entrada: action="ADD", name="Eve", phone=" " (teléfono solo espacios)
Salida esperada:
Si hay .strip() y validación → "Error: phone cannot be empty".
Si no valida → guarda teléfono vacío o inválido; consultas posteriores pueden fallar.
Por qué: campo vacío/espacios es borde.

Caso 3 (código roto)
Entrada: action="DELETE", name="NonExistent"
Salida esperada/efecto:
Debe devolver "Error: contact not found".
Si el código hace contacts.pop(name) sin comprobar, se puede lanzar KeyError (si no se usa segundo arg en pop).
Por qué: intento de borrar clave inexistente sin control provoca excepción.
"""

# Conclusión:
# Las listas de tuplas combinan dos estructuras muy importantes de Python: la mutabilidad de las listas y la estabilidad de las tuplas. 
# Gracias a esto, permiten almacenar conjuntos de datos organizados, donde cada tupla mantiene información fija mientras la lista puede crecer, modificarse o recorrerse fácilmente. 
# Los casos de prueba muestran que este tipo de estructura es muy útil para trabajar con datos relacionados, como pares de coordenadas o registros, 
# pero también evidencian que errores comunes —como tuplas incompletas, tipos incorrectos o datos mal formateados— pueden provocar fallos al intentar acceder o operar sobre sus elementos. En conclusión, las listas de tuplas son una herramienta poderosa y flexible, 
# pero requieren validar el tamaño y el tipo de cada tupla para asegurar que el programa funcione correctamente en todo tipo de situaciones.