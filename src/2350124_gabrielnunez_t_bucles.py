#  Problem 1: Sum of range with for 
user_input = input("Ingresa un valor para n: ")

# Validación 1: verificar si puede convertirse a int
try:
    n = int(user_input)
except:
    print("Error: invalid input")
    exit()

# Validación 2: n debe ser >= 1
if n < 1:
    print("Error: invalid input")
    exit()

# Acumuladores
total_sum = 0
even_sum = 0

# Bucle for para sumar
for i in range(1, n + 1):
    total_sum += i
    if i % 2 == 0:
        even_sum += i

# Salidas
print("Sum 1..n:", total_sum)
print("Even sum 1..n:", even_sum)
