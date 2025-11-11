"""
squares= []
for value in range (0,11):
        square = valure **2
        squares.append(square)
print(squares)
"""
"""
    Una list comprehention comvina el ciclo for y la 
    creeacrion de nuevos elemtnos en una sola linea y automaticamente
    agrega cada nuevo elemto a la lista, es dicir, sin utilizar append.
"""
squares= [value**2 for value in range (0,11)]

# Para los numeros pares entre el 0 y el 100
evensa_range = [value for value in range (0,101,2)]
evens_if= [value for value in range (0,101) if value % 2 ==0]
print(evens_if)