# while infinito
while True:
    try: 
        number = int(input("Ingresa un numero: "))

        if number >=25 and number <=50:
            print("Estas dentro del rango, lo hiciste bien")
            break
        else:
            print("Estas fuerda de rango")
    except ValueError:
        print("Se a introduccido un valor no identificado")