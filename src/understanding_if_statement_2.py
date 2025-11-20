age= 0
try: 
    age= int(input("Escribe tu edad: "))
except:
    age= -1 
    print("Erorr, ingresaste un caracter no valido")

print("Holi Charly")
#
if age >= 100:
    print("Tienes mas de un siglo")
elif age >=18 and age < 100: 
        print("Eres mayor de edad")
elif age >= 0 and age < 18: 
        print("Eres menor de edad")
else:
    print("Tuviste un error")
#
try: 
    age= int(input("¿Cual es tu edad?: "))
except:
    age= -1 
if age<= 4 and age >=0 :
    print("Tu entrada es gratuita")
elif age<=17 and age >=5 : 
        print("Deberas pagar $200")
elif age>=18:       
        print("Deberas pagar $400")
else:
    print("Error, ingresaste un caracter no valido")

# Utilizando varias listas
guisos_disponibles = ["salsa verde", "deshebrada", "mole"]
guisos_a_ordenar= ["deshebrada", "caldo de iguana"]

print("¿Que guisos deseas ordenar?")
for guiso in guisos_a_ordenar:
    print(f"Deseo {guiso}")
    if guiso in guisos_disponibles:
        print(f"Si tenemos {guiso}")
    else:
        print(f"Lo siento, no tenemos {guiso}")
print("Realizando pedido....")