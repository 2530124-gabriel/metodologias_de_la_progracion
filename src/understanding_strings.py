"""
    String variables
    
    Un string es de manera sencilla una seria
    de carcteres. En python, todo lo que se encuentre dentro
    de cinukkas (' ') o dobles (" ") 
    se considerado un string.

    Ejemplos:
        "Esto es un string"
        'Esto tambien es un string'
        'Le dije a un amigo "Python es mi lenguaje favorito" '
        "El lenguaje 'Python lleva el nombre por Monty Python, no por la serpiente' "
"""
name = "Clase de programacion"
print(name)     

# title
print(name.title())

print(name)

"""
    Un metodo es una accion que python puede realizar en un fragmento de datos
o sobre una variable.
    El punto . depues de una variable 
seguido de metodo title () dice que se tiene que ejecutar el meotodo tile()
de la variable name.
    Todos los metodos van seguidos de parentesis
porque en ocaciones necesitan informacion adicional para funcionar, la cual iria dentro
de los parentesis.
En esta ocacion el metodo .title no requiere informacion adicional para funcionar.
"""
print("Metodo upper: ", name.upper())
print("Metodo lower: ", name.lower())
    
# Concatenacion de STRINGS 
first_name= "charly"
last_name= "mercury"
full_name= first_name +" "+ last_name
print(full_name)
print(full_name.title())

# Whitesspaces
"""
    Un whitespace se refiere a cualquier caracter que no se imprime, es decir,
    un espacio, tabuladores y finales de linea. Los whitespaces se utilizan comunmente 
    para organizar las salidas de tal manera que sea mas amigable de leer o ver para el usuario.

    Ejermplo:
        - Tabulador: \t
        - Salto de linea: \n
"""
print("Python")
print("\tPython")
print("\t\tPython")

print("Whitespace es salto de linea")
print("Languagues: \n\tPython\nC\n\tJavasscript")

# Eliminacion de espacios en blanco
programming_languages= " Python "
print(programming_languages)
print(programming_languages.lstrip())
print(programming_languages.rstrip())
print(programming_languages.strip())

# Synta Error con String
message= 'Una fortaleza de python es su comunidad'
print(message)
message= Una fortaleza de python es su comunidad'
print(mesage)