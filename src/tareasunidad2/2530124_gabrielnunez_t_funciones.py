# Gabriel de Jesus Nuñez Rodriguez
# 2530124
# IM- 3
## RESUMEN EJECUTIVO
# Una función en Python es un bloque de código reutilizable que realiza
# una tarea específica y permite organizar mejor un programa. Los parámetros
# son las variables definidas dentro de la función, mientras que los argumentos
# son los valores reales que se envían al llamar dicha función. Separar la
# lógica en funciones facilita la reutilización, la lectura del código y la
# detección de errores. Un valor de retorno permite que una función entregue
# un resultado para seguir trabajando con él, lo cual es más flexible que
# simplemente imprimir. Este documento cubrirá la descripción de cada problema,
# el diseño de funciones, sus entradas y salidas, las validaciones necesarias
# y pruebas básicas para verificar el comportamiento del programa.


# GOOD PRACTICES FOR FUNCTION DESIGN
# - Preferir funciones pequeñas que realicen una sola tarea
#   (principio de responsabilidad única).
# - Evitar repetir código: si se detecta lógica duplicada, debe
#   extraerse en una función para mejorar mantenimiento.
# - Procurar que las funciones sean “puras” cuando sea posible,
#   es decir, mismo input → mismo output, sin modificar variables
#   externas ni depender de estados globales.
# - Documentar cada función con comentarios claros que expliquen
#   qué hace, qué parámetros recibe y qué retorna.
# - Utilizar nombres descriptivos, como calculate_bmi o generate_fibonacci,
#   en lugar de nombres vagos como f1, func o do_it.

"""
--------------------------------------------------
GOOD CODING PRACTICES (SUMMARY)
--------------------------------------------------
- Preferir funciones pequeñas con una sola responsabilidad 
  (Single Responsibility Principle).

- Evitar repetir código: si notas que copias y pegas lógica,
  extrae esa parte en una función reutilizable.

- Intentar que las funciones sean "puras" cuando sea posible:
  mismo input -> mismo output y sin modificar nada externo.

- Documentar con comentarios simples:
  * Qué hace la función
  * Qué parámetros recibe
  * Qué devuelve

- Usar nombres claros y descriptivos para funciones y variables.
--------------------------------------------------
"""

# ================================================================
# 7.1 PROBLEM 1: Rectangle area and perimeter
# ================================================================
"""
Problem 1: Rectangle area and perimeter
Description:
Este programa calcula el área y el perímetro de un rectángulo
usando dos funciones. Los valores se validan antes de llamar
las funciones.

Inputs:
- width (float)
- height (float)

Outputs:
- "Area:" <area_value>
- "Perimeter:" <perimeter_value>

Validations:
- width > 0
- height > 0
Si no se cumplen, mostrar "Error: invalid input".

Test cases:
1) Normal: width=5, height=3 → area=15, perimeter=16
2) Border: width=0.1, height=0.1 → área pequeña
3) Error: width=-5 → "Error: invalid input"
"""


def calculate_area(width, height):
    """Regresa el área de un rectángulo."""
    return width * height


def calculate_perimeter(width, height):
    """Regresa el perímetro de un rectángulo."""
    return 2 * (width + height)


def run_problem_1():
    print("\n--- Problem 1 ---")
    try:
        width = float(input("Width: "))
        height = float(input("Height: "))
    except ValueError:
        print("Error: invalid input")
        return

    if width <= 0 or height <= 0:
        print("Error: invalid input")
        return

    area = calculate_area(width, height)
    perimeter = calculate_perimeter(width, height)

    print("Area:", area)
    print("Perimeter:", perimeter)
""" 
    Test cases:
1) Normal:
   base = 10, altura = 5
   Expected: área = 25.0

2) Border (mínimo válido):
   base = 0.1, altura = 0.1
   Expected: área = 0.005

3) Error:
   base = -3, altura = 5
   Expected: "Error: la base y la altura deben ser positivas."
"""


# ================================================================
# 7.2 PROBLEM 2: Grade classifier
# ================================================================
"""
Problem 2: Grade classifier
Description:
La función classify_grade(score) revisa la calificación numérica
y regresa la letra correspondiente A, B, C, D o F.

Inputs:
- score (0–100)

Outputs:
- "Score:" <score>
- "Category:" <grade_letter>

Validations:
- 0 <= score <= 100

Test cases:
1) Normal: score=85 → "B"
2) Border: score=90 → "A" (límite)
3) Error: score=150 → "Error: invalid input"
"""


def classify_grade(score):
    """Regresa la categoría A/B/C/D/F según el valor numérico."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def run_problem_2():
    print("\n--- Problem 2 ---")
    try:
        score = float(input("Score: "))
    except ValueError:
        print("Error: invalid input")
        return

    if not (0 <= score <= 100):
        print("Error: invalid input")
        return

    grade = classify_grade(score)
    print("Score:", score)
    print("Category:", grade)
"""
Test cases:
1) Normal:
   n = 14
   Expected: "El número es par."

2) Border:
   n = 0
   Expected: "El número es par."   (porque 0 es par)

3) Error:
   n = "hola"
   Expected: "Error: debes ingresar un número entero."

"""


# ================================================================
# 7.3 PROBLEM 3: List statistics (min, max, average)
# ================================================================
"""
Problem 3: List statistics
Description:
La función summarize_numbers(numbers_list) regresa un diccionario
con los valores mínimo, máximo y promedio.

Inputs:
- numbers_text (string como "10,20,30")

Outputs:
- "Min:" <min_value>
- "Max:" <max_value>
- "Average:" <average_value>

Validations:
- Texto no vacío
- Lista no vacía
- Todos elementos numéricos

Test cases:
1) Normal: "10,20,30" → min=10 max=30 average=20
2) Border: "5" → min=max=average=5
3) Error: "10,a,30" → "Error: invalid input"
"""


def summarize_numbers(numbers_list):
    """Regresa dict con min, max y average."""
    return {
        "min": min(numbers_list),
        "max": max(numbers_list),
        "average": sum(numbers_list) / len(numbers_list),
    }


def run_problem_3():
    print("\n--- Problem 3 ---")
    numbers_text = input("Numbers separated by commas: ").strip()

    if numbers_text == "":
        print("Error: invalid input")
        return

    parts = numbers_text.split(",")

    numbers = []
    for p in parts:
        try:
            numbers.append(float(p))
        except ValueError:
            print("Error: invalid input")
            return

    if len(numbers) == 0:
        print("Error: invalid input")
        return

    summary = summarize_numbers(numbers)

    print("Min:", summary["min"])
    print("Max:", summary["max"])
    print("Average:", summary["average"])
"""
Test cases:
1) Normal:
   peso = 70 kg, altura = 1.75 m
   Expected IMC: 22.86 → "Normal"

2) Border:
   peso = 40 kg, altura = 1.50 m
   Expected IMC: 17.77 → "Bajo peso"

3) Error:
   peso = -20, altura = 1.70
   Expected: "Error: el peso y la altura deben ser valores positivos."

"""
# ================================================================
# 7.4 PROBLEM 4: Apply discount list
# ================================================================
"""
Problem 4: Apply discount list
Description:
La función apply_discount crea una nueva lista con los precios
ya descontados, sin modificar la lista original.

Inputs:
- prices_text (string "100,200,300")
- discount_rate (float entre 0 y 1)

Outputs:
- "Original prices:" [...]
- "Discounted prices:" [...]

Validations:
- Lista no vacía
- Todos los precios > 0
- 0 <= discount_rate <= 1

Test cases:
1) Normal: "100,200", 0.10 → [90,180]
2) Border: "5", 0 → [5]
3) Error: "10,-5", 0.2 → "Error: invalid input"
"""


def apply_discount(prices_list, discount_rate):
    """Regresa nueva lista con los precios descontados."""
    discounted = []
    for price in prices_list:
        discounted.append(price * (1 - discount_rate))
    return discounted


def run_problem_4():
    print("\n--- Problem 4 ---")
    prices_text = input("Prices separated by commas: ").strip()
    try:
        discount_rate = float(input("Discount rate (0 to 1): "))
    except ValueError:
        print("Error: invalid input")
        return

    if not (0 <= discount_rate <= 1):
        print("Error: invalid input")
        return

    if prices_text == "":
        print("Error: invalid input")
        return

    parts = prices_text.split(",")
    prices = []

    for p in parts:
        try:
            value = float(p)
            if value <= 0:
                print("Error: invalid input")
                return
            prices.append(value)
        except ValueError:
            print("Error: invalid input")
            return

    discounted = apply_discount(prices, discount_rate)

    print("Original prices:", prices)
    print("Discounted prices:", discounted)
"""
1) Normal

Entrada:

prices_text = "100,200"

discount_rate = 0.10

Salida esperada:

Original prices: [100, 200]

Discounted prices: [90, 180]

2) Border (mínimo válido)

Entrada:

prices_text = "5"

discount_rate = 0

Salida esperada:

Original prices: [5]

Discounted prices: [5]

3) Error (precio negativo)

Entrada:

prices_text = "10,-5"

discount_rate = 0.2

Salida esperada:

Error: invalid input

"""

# ================================================================
# 7.5 PROBLEM 5: Greeting with default parameters
# ================================================================
"""
Problem 5: Greeting function with default parameters
Description:
La función greet(name, title="") construye un saludo opcionalmente
con un título antes del nombre.

Inputs:
- name (string)
- title (string opcional)

Outputs:
- "Greeting:" <message>

Validations:
- name no vacío

Test cases:
1) Normal: name="Alice", title="Dr." → "Hello, Dr. Alice!"
2) Border: name="Bob", title="" → "Hello, Bob!"
3) Error: name="   " → "Error: invalid input"
"""


def greet(name, title=""):
    """Regresa un mensaje de saludo."""
    full = name if title == "" else f"{title} {name}"
    return f"Hello, {full}!"


def run_problem_5():
    print("\n--- Problem 5 ---")
    name = input("Name: ").strip()
    title = input("Title (optional): ").strip()

    if name == "":
        print("Error: invalid input")
        return

    message = greet(name, title)
    print("Greeting:", message)
"""
1) Normal

Entrada:

name = "Alice"

title = "Dr."

Salida esperada:

Greeting: Hello, Dr. Alice!

2) Border (sin título)

Entrada:

name = "Bob"

title = ""

Salida esperada:

Greeting: Hello, Bob!

3) Error (nombre vacío)

Entrada:

name = " "

title = "Eng."

Salida esperada:

Error: invalid input
"""
# ================================================================
# 7.6 PROBLEM 6: Factorial function
# ================================================================
"""
Problem 6: Factorial
Description:
La función factorial(n) calcula n! usando un método iterativo.
La validación asegura que n es entero y >=0.

Inputs:
- n (int)

Outputs:
- "n:" <n>
- "Factorial:" <value>

Validations:
- n entero
- n >= 0
- n <= 20 (para evitar números muy grandes)

Test cases:
1) Normal: n=5 → 120
2) Border: n=0 → 1
3) Error: n=-3 → "Error: invalid input"
"""


def factorial(n):
    """Regresa n! usando un método iterativo."""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def run_problem_6():
    print("\n--- Problem 6 ---")
    try:
        n = int(input("n: "))
    except ValueError:
        print("Error: invalid input")
        return

    if n < 0 or n > 20:
        print("Error: invalid input")
        return

    f = factorial(n)
    print("n:", n)
    print("Factorial:", f)

"""
Casos de prueba

1) Normal

Entrada:

n = 5

Salida esperada:

Factorial: 120

2) Border (mínimo válido)

Entrada:

n = 0

Salida esperada:

Factorial: 1

3) Error (valor inválido o fuera de rango)

Entrada:

n = -3

Salida esperada:

Error: invalid input
"""
# ================================================================
# MAIN (MENÚ PARA PROBAR CADA PROBLEMA)
# ================================================================
def main():
    print("\n--- PROGRAM START ---")
    print("1) Rectangle area")
    print("2) Grade classifier")
    print("3) List statistics")
    print("4) Apply discount")
    print("5) Greeting")
    print("6) Factorial")

    option = input("Select problem (1-6): ")

    if option == "1":
        run_problem_1()
    elif option == "2":
        run_problem_2()
    elif option == "3":
        run_problem_3()
    elif option == "4":
        run_problem_4()
    elif option == "5":
        run_problem_5()
    elif option == "6":
        run_problem_6()
    else:
        print("Invalid option.")


if __name__ == "__main__":
    main()


# --------------------------------------------------------------
# CONCLUSIONES
# El uso de funciones permitió organizar mejor el código, separando
# la lógica principal de las operaciones específicas y facilitando
# la reutilización en varios problemas. Devolver valores mediante
# return resultó más útil que solo imprimirlos, ya que permitió
# almacenar, combinar y procesar resultados desde otras partes del
# programa. También, los parámetros y valores por defecto hicieron
# que las funciones fueran más flexibles y adaptables a diferentes
# escenarios. En general, encapsular cálculos repetidos y validaciones
# dentro de funciones simplificó el diseño y reforzó la diferencia
# entre la lógica central del programa y las funciones de apoyo.
# --------------------------------------------------------------

# --------------------------------------------------------------
# REFERENCIAS
# 1) Python Documentation – Defining Functions and Calling Functions:
#    https://docs.python.org/3/tutorial/controlflow.html#defining-functions
# 2) Python Documentation – Built-in Functions and Standard Types:
#    https://docs.python.org/3/library/functions.html
# 3) Tutorial de Programación en Python – Funciones, parámetros y retorno:
#    (Ej. W3Schools Python Functions)
# 4) Libro: "Automate the Boring Stuff with Python", capítulos sobre funciones
#    y buenas prácticas de modularidad.
# 5) Apuntes de clase y materiales oficiales de la asignatura de Programación,
#    sección: “Funciones, modularidad y reutilización de código”.
# --------------------------------------------------------------
