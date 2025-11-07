# Trabajo con listas
"""
    Recorrer una lista sin importar la cantidad 
    de elementos que tenga.
"""

magicians= ["ron", "hermion", "harry", "goku", "andrix"]
print(magicians[0], magicians[1], magicians[2])

for magician in magicians: 
    print(magician)
    print(magician.upper())
    print(f"{magician.title()} ese fue un gran hechizo.")
    print(f"\t {magician.lower()}No podemos esperar para ver el siguiente hechizo")

print("Gracias a todos, fue un gran espectaculo")

"""
    Identación
    
    Python utiliza la identacion para determinar cuando
    una linea de codigo esta conectada a la linea de codigo anterior.

    Basicamente, se utlilizan 4 espacios en blanco para obligarnos
    a escribir codigo ordenado y estructurado.
"""
#No olvidemos identar
magicans = ["alice", "david", "carolina"]
for magican in magicans:
    print(magican) 
print(f"I cant wait to see the next magican's trick!, {magican.title()}.")

# Identacion inncesaria
message = "Hello Python world!"
    print(message)