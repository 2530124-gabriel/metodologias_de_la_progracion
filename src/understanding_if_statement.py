cars = ['audi', 'bmw', "chevrolet", "corvette", "tesla"]
for car in cars:
    if car == "bmw" or car == "tesla" or car == "audi":
        print(car.upper())
    else:
        print(car)
print("-----conditional-----")
#Condicionales: El condicional es el corazon de un if
#Condicional True
car = 'bmw'
print(car=='bmw')
car_2 = 'Audi'
print(car_2 =='audi') # salida -> False
#Conditional False
car_2 = 'Audi'
print(car_2.lower()=='audi') # salida -> True

#Condicional != para determinar desigualdad
requested_topping= "mushrooms" # -> string
if requested_topping != 'anchovies': # -> True
    print("Hold the anchovies")

# Comparaciones numericas
age = 18 # -> int
print(age==18) # -> True

answer= 17 
if answer != 42:
    print("Esa no es la respuesta correcta. Intenta otra vez")

age= 19
print(age<21) #True
print(age<=21)# True
print(age>21) #False
print(age>=21)#False

#.Multiple conditions
age_0= 22
age_1 = 18
print("Multiples condiciones")
print("Operacion and - pseint (Y)")
print(age_0>=21 and age_1 >=21) # False
print(age_0>=21 and age_1 >=18) # True

print("Operacion or - pseint (0)")
print(age_0>=21 or age_1 >=21) # True
print(age_0>=23 or age_1 >=21) # False

# ¿Como nos preguntamos si algun valor esta
# en una lista?
requested_topping = ['mushrooms', 'onion', 'pineapple']
print('mushrooms' in requested_topping) # -> True
print('pepperoni' in requested_topping) # -> False

# A valued not in a list
banned_users = ["gabriel", "max", "andrix", 'quevedo', 'cristo', 'angel']
user = "pedro"
print(user not in banned_users)

# Variables de tipo booleano
game_activate = True
can_edit= False

"""
    if statement

    if condition:
        do something
    
    if condition:
        do something (True)
    else: 
        do something (False)

"""

# Preguntar la edad del usuario 
# y decirle si tiene la edad
# suficiente para votar
# input("") -> str
age = int(input("\n\nEscribe tu edad: "))
print(f"\nTu edad es: {age}")

if age>=18:
    print("Tienes la edad suficiente para votar")
else:
    print("Lo siento, eres demasiado joven para votar")