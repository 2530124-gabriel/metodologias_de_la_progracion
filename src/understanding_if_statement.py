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
