# Numbers

"""
    Eneteros
        Los podemos sumer (+), restar (-), multiplicar (*) y dividir (/)
        Le podemos aplicar potencias(**2, **3, **4, ...)

"""
number_1 = 35
number_2 = 15
suma = number_1+number_2
resta= number_1-number_2
multiplicar= number_1*number_2
division= number_1/number_2
potencia = number_1**2
modulo = number_1%number_2
print("Suma: ", suma, type(suma))
print("Resta: ", resta, type(resta))
print("Multiplicacion: ", multiplicar, type(multiplicar))
print("Division: ", division, type(division))
print("Potencia:", potencia, type (potencia))
print("Modulo", modulo, type(modulo))

"""
    Jeraquia de operaciones

    2+3*4 --> 14

    (2+3)* 4 --> 20
"""
"""
    Floats
        Python llama Floats a cualquier numero con un punto decimal.
        Los podemos sumer (+), restar (-), multiplicar (*) y dividir (/)
        Les podemos aplicar potencias (**2, **3, **4, ...)
"""
print(0.1 + 0.1)
print(0.2 - 0.2)
print(0.1 * 2)
print(0.1 + 0.1)

# Imprimir la edad de alguien
age = 33
message= "Charly tiene" + " "+ str(age) + " " + "años"
print (message)

"""
Type error python no puede reconocer el tipo de informacion que se esta utilizando
"""