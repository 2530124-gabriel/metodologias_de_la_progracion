"""
    El usuario va a tener un maximo de intentos para colocar bien el pin.
    
    Si usuario sobre pasa este maximo de intentos
    se le va a bloquear la cuneta y el acceso.
"""
CORRECT_PIN = "1234"
MAX_ATTEMPTS = 3
attempt = 0
remaning_attempts = MAX_ATTEMPTS

while attempt < MAX_ATTEMPTS:
    user_input = input("Ingresa tu pin: ")

    if user_input == CORRECT_PIN:
        print("Bienvenido")
        break   
    else:
        attempt+=1
        remaning_attempts = MAX_ATTEMPTS - attempt
        if remaning_attempts > 0:
            print("Ingresaste un pin no valido")
            print(f"Te quedan {remaning_attempts} de intentos")
        else:
            print("Cuenta bloqueada.")