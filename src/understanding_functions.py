"""
    Estrucutura de una funcion
    
    def nombre_function:
        '''
            docstrings
        '''
        actions
"""             
# Ejemplo de una funcion que genere el nombre completo
# de una persona y lo regrese.

def create_full_name(first_name, middle_name, last_name): 
    full_name = f"{first_name.strip()} {middle_name.strip()} {last_name.strip()}".title()
    return full_name

user_first_name = input("Dame tu primer nombre: ")
user_middle_name = input("Dame tu segundo nombre: (Sino tienes segundo nombre dale a enter) ")
user_last_name = input("Dame tus apellido: ")

# Parametros posicionales
generated_fullname = create_full_name(
    user_first_name.strip().lower(), 
    user_middle_name.strip().lower(), 
    user_last_name.strip().lower())
print(generated_fullname)

# argumentos llave
generated_fullname_2 = create_full_name(
    middle_name = user_middle_name,
    first_name = user_first_name, 
    last_name = user_last_name)

# args en funciones
# kwargs en funciones
# Manejo de datos(.txt, csv, json, excel, word, pdf)
# args via consola (sys)
# cli en python - comand line interface
# testing - Casos prueba (borde, validos, invalidos)