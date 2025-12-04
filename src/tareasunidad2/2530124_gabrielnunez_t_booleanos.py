# Gabriel de Jesus Nuñez Rodriguez
# 2530124
# IM- 3
## Resuemen ejecutivo
###Los booleanos son un tipo de dato fundamental en Python que solo puede tomar dos valores: True o False, 
### usados principalmente para tomar decisiones dentro de un programa. 
### Este tipo de dato surge del resultado de comparaciones (>, <, ==, !=, etc.) y de expresiones lógicas, utilizando operadores como and, or y not. 
### Los booleanos permiten controlar el flujo del código mediante estructuras como if, elif y while.
### Es importante comprender que prácticamente todo valor en Python tiene un equivalente booleano: 
### algunos valores se consideran False (como 0, "", [], None) y el resto se consideran True. 
### El manejo adecuado de booleanos es esencial para validar datos, crear condiciones, filtrar información y construir algoritmos más robustos. 
### Este documento cubrirá qué es un booleano, cómo se generan, operadores lógicos, valores truthy/falsy y ejemplos prácticos de uso.

## Problem 1: Temperature converter and range flag
print("Problem 1: Temperature converter and range flag")

temp_c = input("Ingresa la temperatura en Celsius: ")

# validar vacío
if temp_c == "":
    print("Entrada vacía. Intenta de nuevo.")
else:
    # convertir a float
    try:
        temp_c = float(temp_c)
    except ValueError:
        print("Entrada no válida. Debes ingresar un número.")
    else:
        # convertir
        temp_f = (temp_c * 9/5) + 32
        temp_k = temp_c + 273.15

        # validar Kelvin físico
        if temp_k < 0:
            print("Temperatura físicamente imposible.")
        else:
            # definir booleano
            is_high_temperature = (temp_c >= 30)

            # imprimir
            print("Fahrenheit:", temp_f)
            print("Kelvin:", temp_k)
            print("High temperature:", is_high_temperature)
# casos de pruebas
# caso 1
""""
Entrada simulada:

25


Proceso esperado:

temp_c = 25

temp_k = 298.15 (≥ 0, válido)

temp_f = 77.0

is_high_temperature = False (25 < 30)

Salida esperada:

Fahrenheit: 77.0
Kelvin: 298.15
High temperature: False
"""

# 2. Caso Borde
"""
Entrada simulada:

-273.15


Proceso esperado:

temp_c = -273.15

temp_k = 0.0 (límite mínimo, válido)

temWS
is_high_temperature = False

Salida esperada:

Fahrenheit: -459.66999999999996
Kelvin: 0.0
High temperature: False
"""

# 3. Caso Error
"""
A) Error físico (Kelvin negativo)

Entrada simulada:

-300


Proceso esperado:

temp_k = -26.85 → no válido

El programa debe mostrar error antes de convertir a Fahrenheit.

Salida esperada:

Error: invalid input

# Error de formato (cae en el except)

Entrada simulada:

hola


Salida esperada:

Error: invalid input

"""


## Problem 2: Work hours and overtime payment
print("\n Problem 2: Work hours and overtime payment")
hours_worked = float(input("Ingresa las horas trabajadas en la semana: "))
hourly_rate = float(input("Pago por hora: "))

# Validaciones
if hours_worked < 0 or hourly_rate <= 0:
    print("Error: invalid input")
else:
    # Separación de horas regulares y extra
    regular_hours = min(hours_worked, 40)
    overtime_hours = max(hours_worked - 40, 0)

    # Cálculos
    regular_pay = regular_hours * hourly_rate
    overtime_pay = overtime_hours * hourly_rate * 1.5
    total_pay = regular_pay + overtime_pay

    # Booleano
    has_overtime = hours_worked > 40

    # Salidas
    print("Regular pay:", regular_pay)
    print("Overtime pay:", overtime_pay)
    print("Total pay:", total_pay)
    print("Has overtime:", has_overtime)
# casos de pruebas 
# caso 1
""" 
Hours worked: 45
Hourly rate: 20

Proceso esperado:

regular_hours = 40

overtime_hours = 5

regular_pay = 40 × 20 = 800

overtime_pay = 5 × 20 × 1.5 = 150

total_pay = 950

has_overtime = True

# salida 
Regular pay: 800.0
Overtime pay: 150.0
Total pay: 950.0
Has overtime: True



"""
# caso 2 borde 
"""
Hours worked: 40
Hourly rate: 15
Proceso esperado:

overtime_hours = 0

regular_pay = 600

overtime_pay = 0

total_pay = 600

has_overtime = False
# salida
Regular pay: 600.0
Overtime pay: 0.0
Total pay: 600.0
Has overtime: False



"""
# caso 3 error 
"""
Hours worked: -5
Hourly rate: 18
Salida esperada:

Error: invalid input


"""

##  Problem 3: Discount eligibility with booleans
# Entradas
purchase_total = float(input("Total de la compra: "))
is_student_text = input("¿Es estudiante? (YES/NO): ").upper()
is_senior_text = input("¿Es adulto mayor? (YES/NO): ").upper()

# Validaciones
if purchase_total < 0:
    print("Error: invalid input")
    exit()

if is_student_text not in ("YES", "NO") or is_senior_text not in ("YES", "NO"):
    print("Error: invalid input")
    exit()

# Conversión a booleanos
is_student = (is_student_text == "YES")
is_senior = (is_senior_text == "YES")

# Regla para descuento
discount_eligible = is_student or is_senior or (purchase_total >= 1000.0)

# Cálculo del total final
if discount_eligible:
    final_total = purchase_total * 0.9   # 10% de descuento
else:
    final_total = purchase_total

# Salidas
print("Discount eligible:", discount_eligible)
print("Final total:", final_total)

# casos de pruebas
# cas0 1
"""
Entrada simulada:

Purchase total: 500
Student (YES/NO): YES
Senior (YES/NO): NO


Proceso esperado:

purchase_total = 500

is_student = True

is_senior = False

discount_eligible = True (porque es estudiante)

final_total = 500 * 0.9 = 450

Salida esperada:

Discount eligible: True
Final total: 450.0
"""
 #2. Caso Borde (límite)
"""
A) Justo en el límite del descuento por monto

Entrada simulada:

Purchase total: 1000
Student (YES/NO): NO
Senior (YES/NO): NO


Proceso esperado:

purchase_total = 1000

is_student = False

is_senior = False

discount_eligible = True (porque total ≥ 1000)

final_total = 1000 * 0.9 = 900

Salida esperada:

Discount eligible: True
Final total: 900.0
"""
# 3. Caso Error
"""
A) Monto inválido

Entrada simulada:

Purchase total: -50
Student (YES/NO): NO
Senior (YES/NO): NO


Salida esperada:

Error: invalid input

B) Texto inválido en YES/NO (cae en la validación)

Entrada simulada:

Purchase total: 500
Student (YES/NO): maybe
Senior (YES/NO): NO


Salida esperada:

Error: invalid input

C) Error de formato que activa el except

Entrada simulada:

Purchase total: hola
Student (YES/NO): YES
Senior (YES/NO): NO


Salida esperada:

Error: invalid input




"""
# Problem 4: Basic statistics of three integers

print("\n Problem 4: Basic statistics of three integers")
 
    try:
        n1 = int(input("Ingresa el primer numero entero: "))
        n2 = int(input("Ingresa el segundo numero entero: "))
        n3 = int(input("Ingresa el tercer numero entero: "))
    except ValueError:
        print("Error: invalid input")
        exit()
    # Cálculos
    maximum = max(n1, n2, n3)
    minimum = min(n1, n2, n3)
    promedio = (n1 + n2 + n3) / 3
    suma = n1 + n2 + n3
    all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)
    print("Maximum:", maximum)
    print("Minimum:", minimum)
    print("Average:", promedio)
    print("Sum:", suma)
    print("All even:", all_even)

# caso de pruebas
# caso 1
"""
1. Caso Normal

Entrada simulada:

Enter integer 1: 4
Enter integer 2: 7
Enter integer 3: 10


Proceso esperado:

sum = 4 + 7 + 10 = 21

average = 21 / 3 = 7.0

max = 10

min = 4

all_even = False (solo 4 y 10 son pares)

Salida esperada:

Sum: 21
Average: 7.0
Max: 10
Min: 4
All even: False
"""
# 2. Caso Borde (con valores iguales)
"""
Entrada simulada:

Enter integer 1: 5
Enter integer 2: 5
Enter integer 3: 5


Proceso esperado:

sum = 15

average = 5.0

max = 5

min = 5

all_even = False (5 es impar)

Salida esperada:

Sum: 15
Average: 5.0
Max: 5
Min: 5
All even: False
"""
#3. Caso Error
"""
A) Formato inválido (cae en el except)

Entrada simulada:

Enter integer 1: hola
Enter integer 2: 8
Enter integer 3: 3


Salida esperada:

Error: invalid input

B) Otro error válido (número decimal cuando esperaba entero)

Entrada simulada:

Enter integer 1: 4.5
Enter integer 2: 2
Enter integer 3: 8


Salida esperada:

Error: invalid input


"""    

## Problem 5: Loan eligibility (income and debt ratio)
print("\n Problem 5: Loan eligibility (income and debt ratio)")
# Entradas con validación
try:
    monthly_income = float(input("Ingresa el ingreso mensual: "))
    monthly_debt = float(input("Ingresa la deuda mensual: "))
    credit_score = int(input("Ingresa el puntaje de crédito: "))
except ValueError:
    print("Error: invalid input")
    exit()

# Validaciones
if monthly_income <= 0 or monthly_debt < 0 or credit_score < 0:
    print("Error: invalid input")
    exit()

# Cálculo del debt ratio
debt_ratio = monthly_debt / monthly_income

# Reglas de elegibilidad
eligible = (
    monthly_income >= 8000.0 and
    debt_ratio <= 0.4 and
    credit_score >= 650
)

# Salidas
print("Debt ratio:", debt_ratio)
print("Eligible:", eligible)
# casos de pruebas
# caso 1
"""
Entrada simulada:

Monthly income: 9000
Monthly debt: 2000
Credit score: 700


Proceso esperado:

debt_ratio = 2000 / 9000 = 0.222...

eligible = True

income ≥ 8000 ✔

debt_ratio ≤ 0.4 ✔

credit_score ≥ 650 ✔

Salida esperada:

Debt ratio: 0.2222222222222222
Eligible: True
"""
# 2. Caso Borde (límite exacto)
"""
Entrada simulada:

Monthly income: 8000
Monthly debt: 3200
Credit score: 650


Proceso esperado:

debt_ratio = 3200 / 8000 = 0.4

eligible = True

income ≥ 8000 ✔

debt_ratio ≤ 0.4 ✔

credit_score ≥ 650 ✔

Salida esperada:

Debt ratio: 0.4
Eligible: True
"""
# 3. Caso Error
"""
A) Valores inválidos

Entrada simulada:

Monthly income: 0
Monthly debt: 500
Credit score: 700


Salida esperada:

Error: invalid input

B) Formato inválido (cae en el except)

Entrada simulada:

Monthly income: hola
Monthly debt: 500
Credit score: 700


Salida esperada:

Error: invalid input

"""

## Problem 6: Body Mass Index (BMI) and category flag
print("\n Problem 6: Body Mass Index (BMI) and category flag")
# Entradas con validación
try:
    weight_kg = float(input("Ingresa tu peso en kg: "))
    height_m = float(input("Ingresa tu estatura en metros: "))
except ValueError:
    print("Error: invalid input")
    exit()

# Validaciones
if weight_kg <= 0 or height_m <= 0:
    print("Error: invalid input")
    exit()

# Cálculo del BMI
bmi = weight_kg / (height_m * height_m)
bmi_redondeado = round(bmi, 2)

# Booleanos según los rangos
is_underweight = bmi < 18.5
is_normal = 18.5 <= bmi < 25.0
is_overweight = bmi >= 25.0

# Salidas
print("BMI:", bmi_redondeado)
print("Underweight:", is_underweight)
print("Normal:", is_normal)
print("Overweight:", is_overweight)
# caso de pruebas
"""
1. Caso Normal (BMI dentro del rango saludable)

Entrada simulada:

Weight (kg): 70
Height (m): 1.75


Proceso esperado:

bmi = 70 / (1.75²) = 22.857…

bmi_r = 22.86

is_underweight = False

is_normal = True

is_overweight = False

Salida esperada:

BMI: 22.86
Underweight: False
Normal: True
Overweight: False
"""
# 2. Caso Borde (límite exacto entre normal y sobrepeso)
"""
Entrada simulada:

Weight (kg): 62
Height (m): 1.57


Cálculo:

bmi = 62 / (1.57²) ≈ 25.15 → ya entra en Overweight

Salida esperada:

BMI: 25.15
Underweight: False
Normal: False
Overweight: True


(Este es un caso borde porque está muy cerca del límite de 25.0)
"""
# 3. Caso Error
""" 
A) Peso inválido

Entrada simulada:

Weight (kg): -50
Height (m): 1.70


Salida esperada:

Error: invalid input

B) Formato inválido (cae en el except)

Entrada simulada:

Weight (kg): hola
Height (m): 1.70


Salida esperada:

Error: invalid input

"""
# 8. CONCLUSION
# En este módulo pude ver cómo los enteros y los flotantes trabajan juntos para realizar cálculos reales,
# permitiendo manejar desde horas trabajadas hasta índices como el BMI o razones de deuda. También entendí
# cómo las comparaciones generan valores booleanos que después permiten tomar decisiones mediante estructuras
# if, lo cual es esencial para evaluar reglas, rangos o condiciones de elegibilidad. Aprendí la importancia
# de validar rangos y evitar errores comunes como dividir entre cero, lo que garantiza programas seguros y robustos.
# Además, comprendí mejor cómo diseñar condiciones combinadas con and, or y not para crear reglas más complejas
# sin perder claridad. Finalmente, noté que estos mismos patrones lógicos se repiten en muchos problemas reales,
# como cálculos de nómina, descuentos, préstamos y evaluaciones de datos.

