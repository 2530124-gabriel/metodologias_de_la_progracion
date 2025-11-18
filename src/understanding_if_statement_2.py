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




