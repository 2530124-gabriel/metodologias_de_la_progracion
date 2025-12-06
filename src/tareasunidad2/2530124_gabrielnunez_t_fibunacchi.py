# Gabriel de Jesus Nuñez Rodriguez
# 2530124
# IM- 3
## RESUMEN EJECUTIVO

# La serie de Fibonacci es una secuencia numérica donde cada término
# resulta de la suma de los dos anteriores, iniciando normalmente en 0 y 1.
# Calcular la serie hasta un número de términos n significa generar
# los primeros n valores siguiendo esta regla.
# Este programa leerá el valor de n, realizará una validación básica
# y generará la serie completa de Fibonacci hasta esa cantidad.

# --------------------------------------------------------------
# Problem: Fibonacci series generator
# Description:
# Program that reads an integer n and prints the first n terms
# of the Fibonacci series starting at 0 and 1.
#
# Inputs:
# - n (int; number of terms to generate)
#
# Outputs:
# - "Fibonacci series:" followed by the n terms separated
#   by spaces or commas
#
# Validations:
# - n must be an integer
# - n must be >= 1
# - (Optional) n must be <= 50
#
# Test cases:
# 1) Normal: n = 7 → expected series: 0 1 1 2 3 5 8
# 2) Border: n = 1 → expected series: 0
# 3) Error: n = "abc" → expected message: "Error: invalid input"
#
# --------------------------------------------------------------


print("\nFibonacci Series Generator")
n_input = input("Enter number of terms: ").strip()

# Validar si es entero
try:
    n = int(n_input)
except:
    print("Error: invalid input")
    exit()

# Validaciones adicionales
if n < 1 or n > 50:
    print("Error: invalid input")
    exit()

# Generación de la serie de Fibonacci
fibonacci = []

if n >= 1:
    fibonacci.append(0)
if n >= 2:
    fibonacci.append(1)

# Generar términos restantes
a, b = 0, 1
for _ in range(3, n + 1):
    c = a + b
    fibonacci.append(c)
    a, b = b, c

# Salida
print("Fibonacci series:", *fibonacci)
