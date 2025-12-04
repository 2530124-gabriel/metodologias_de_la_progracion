# while infinito
while True:
    try: 
        number = int(input("Ingresa un numero ente 10 y 20: "))

        if number >=10 and number <=20:
            print("Estas dentro del rango, lo hiciste bien")
            break
        else:
            print("Estas fuerda de rango")
    except ValueError:
        print("Se a introduccido un valor no identificado")
    except KeyboardInterrupt:
        print("\nProceso interrumpido por el usuario.")
        break

print("Programa terminado.")

# figunachi
number_one = 0
number_two = 1
while number_two <= 1597:
    print(number_one, number_two, end= " ")
    number_one= number_one + number_two
    number_two= number_one + number_two


number_tree = 0
number_fourd = 1
while number_two <= 1597:
    print(number_tree, number_fourd, end = " ")
    number_tree= number_tree + number_fourd
    number_fourd = number_tree + number_fourd