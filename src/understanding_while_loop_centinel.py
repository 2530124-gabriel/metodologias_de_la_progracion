"""
    Docstring for understanding while loop with centinel value

    Un programa que:
     - Cuente cuandos numeros ha ingresado el usuario
     - Realice la suma de estos numeros
     - Me diga cual es el minimo de los numeros ingresados
     - Me diga cual es el maxico de los numeros ingresados
"""
counter = 0
sum_quant_numbers = 0.0
minimun = None
maximum = None

while True:
    print("Escribe exit para salir")
    user_input= input("Ingrsa una cantidad (MXN): ")
    
    if user_input == "exit":
        break
    try:
        value = float(user_input)
    except ValueError:
        print("Erorr ingresaste un caracter invalido")
    except KeyboardInterrupt:
        print("Salida manual")
        break  
    counter = counter + 1 # Por cada numero se suma al contador
    sum_quant_numbers += value

    if minimun is None or value < minimun:
        minimun = value

    if maximum is None or value > maximum: 
        maximun = value

print("Cantidad de numeros ingresados: ", counter)
print("Suma de los numeros ingresados: ", sum_quant_numbers)
print("Minimo de los numeros ingresados: ", minimun)
print("Maximo de los numeros ingresados: ", maximum)
