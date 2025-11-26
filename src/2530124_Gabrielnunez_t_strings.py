# Gabriel de Jesus Nuñez Rodriguez
# 2530124
# IM- 3
## Resuemen ejecutivo
### Los strings en Python son un tipo de dato que representa texto y son inmutables, 
### lo que significa que no se pueden modificar directamente. 
### Con ellos se pueden hacer operaciones básicas como concatenar textos, obtener su longitud, extraer sub-cadenas con slicing, 
### buscar patrones y reemplazar partes específicas. Es importante validar y normalizar el texto de entrada para evitar errores, 
### por ejemplo en correos, nombres o contraseñas, y asegurar que los datos sean consistentes. En mi documento explicaré cada problema, 
### cómo diseñé las entradas y salidas y qué validaciones utilicé. También mostraré el uso de los métodos de string en Python con sus casos de prueba y el código correspondiente.

## Problem 1: Full name formatter (name + initials)
full_name = (" Gabriel de jesus Nuñez rodriguez ").strip()
formatted_name = full_name.title()
initials = ''
for w in full_name.split():
    initials += w[0].upper() + '.'
#### Imprime nombre
print(formatted_name)
#### Imprime iniciales
print("Initials:", initials)

## Problem 2: Simple email validator (structure + domain)
print("\nProblem 2: Simple email validator")
email_text= (" gabogahi@gmailcom ").strip()
if email_text == "": 
    print("false")
elif email_text.count("@") != 1:
    print("false")
elif email_text == " ":
    print("false")
else:
    at_email= email_text.find("@")
    domain = email_text[at_email + 1:] 
    if "." not in domain:
        print("false")
    else:
        print("true")

## Problem 3: Palindrome checker (ignoring spaces and case)
print("\nProblem 3: Palindrome checker")
palabra= ("pala alap").strip()
palabra_sin = palabra.replace(" ", "").lower()
if palabra_sin == palabra_sin[::-1]:
    print("Es un palindromo")
elif len(palabra_sin) < 3:
    print("La palabra es muy corta para ser un palindromo")
else:
    #Salida
    print("No es un palindromo")

##  Problem 4: Sentence word stats (lengths and first/last word)
print("\nProblem 4: Sentence word stats")
Oracion= ("  La vida es bella  ").strip()
palabras= Oracion.split()

if Oracion == "":
    print("La oracion esta vacia")
else:
    num_de_palabras = len(palabras)
    shortest_word = palabras[0]
    longest_word = palabras[0]
    for w in palabras:
        if len(w) < len(shortest_word):
            shortest_word = w
        if len(w) > len(longest_word):
            longest_word = w
    #Salidas
    print("Numero de palabras:", num_de_palabras)
    print("Palabra mas corta:", shortest_word)
    print("Palabra mas larga:", longest_word)
    print("Primera palabra:", palabras[0])
    print("Ultima palabra:", palabras[-1])

##  Problem 5: Password strength classifier

print("\nProblem 5: Password strength classifier")
password= ("gabriel121")
# Validacion
if password == "": 
    print("Contraseña vacia") 
else: # Clasificacion
    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False
    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        else: # Caracter especial
            has_symbol = True
    if has_upper and has_lower and has_digit and has_symbol and len(password) >= 8:
        print("Contraseña fuerte") # Fuerte
    elif has_upper or has_lower and has_digit and len(password) > 8:
        print("Contraseña media") # Media
    else:
        print("Contraseña debil") # Debil

## Problem 6:  Product label formatter (fixed-width text)
print("\nProblem 6: Product label formatter")
product_name = " Cereza ".strip()
price_value = 5

if product_name == "":
    print("Nombre de producto invalido")
else:
    try:
        price = float(price_value)
        if price < 0:
            print("Precio invalido")
        else:
             # Crear etiqueta base
            label = f"Product: {product_name} | Price: ${price_value}"

            # Recortar si se pasa de 30
            label = label[:30]

            # Rellenar si es corta
            while len(label) < 30:
                label += " "

            print("Label:", f"'{label}'")  # comillas para ver espacios
    except:
        print("Precio inválido")

# 8. CONCLUSION
# El manejo de strings es fundamental en cualquier programa porque casi toda
# entrada del usuario llega en forma de texto, por eso es necesario limpiarlo
# con funciones como strip(), lower(), replace() y split(). Normalizar el texto
# permite comparaciones correctas y evita errores, ya que dos cadenas pueden
# parecer iguales pero diferir en espacios o mayúsculas. Las validaciones son
# clave para detectar datos incompletos o incorrectos antes de procesarlos.
# Además, aprendí que los strings son inmutables, por lo que cada operación
# genera uno nuevo, y por eso el slicing es útil para extraer o modificar partes
# específicas sin alterar la cadena original.


# 9. REFERENCIAS
# Python Documentation – Built-in Types: Text Sequence Type (str).
# https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str
#
# Python String Methods – Official Documentation.
# https://docs.python.org/3/library/stdtypes.html#string-methods
#
# Real Python – Working With Strings in Python (Tutorial).
# https://realpython.com/python-strings/
#
# W3Schools – Python String Tutorial.
# https://www.w3schools.com/python/python_strings.asp
#
# Curso de Algoritmos y Programación – Manejo de cadenas y validación de datos.
# Apuntes académicos sobre buenas prácticas en entrada y limpieza de texto.

