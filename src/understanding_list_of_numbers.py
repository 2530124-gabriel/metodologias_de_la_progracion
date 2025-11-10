"""
    Las listas tambien pueden almacenar 
    numero y de echo, son ideales para esto.
    Python ofrece una gran cantidad de herramientas 
    que ayudan a trabajar eficientemente con listas
    de numeros.
"""
# Metodo built-in range()
"""
    El metodo range() nos ayuda a crear facilmente 
    series de numeros.
    Ejemplos: 

"""
print("Numeros del 0 al 9")
for value in range (0,10): # 10 numeros del 0 al 9
    print(value)

print("Numeros del 1 al 9")
for value in range (1,10): # 10 numeros del 1 al 9
    print(value)

print("Numeros Impares del 1 al 9")
for value in range (1,10,2): # 10 numeros del 1 al 9 con paso de 2
    print(value)
odd_numbers= list(range (1,10,2))
print(odd_numbers)
print("Numeros Pares del 1 al 9")
for value in range (0,10,2): # 10 numeros del 0 al 9 con paso de 2
    print(value)
event_numbers= list(range (0,10,2))
print(event_numbers)
print("Tabla del 9")
for value in range (0,91,9): # Tabla del 9
    print(value)

# Cuadrados de los primeros 10 numeros
squares= [] # Lista vacia
for number in range (1,11):
    square= number**2
    squares.append(square)      
print(squares)

## Mas metodos built-in 
# Meotodo min()
digits= [1,2,3,4,5,6,7,8,9,0]
print(min(digits)) # Salida: 0
# Metodo max()
digits= [1,2,3,4,5,6,7,8,9,0]
print(max(digits)) # Salida: 9
# Metodo sum()  
digits= [1,2,3,4,5,6,7,8,9,0]
print(sum(digits)) # Salida: 45