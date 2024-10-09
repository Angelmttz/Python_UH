def suma(a , b):
    return a + b

def resta(a , b):
    return a - b

def multi(a , b):
    return a * b

def division(a ,b):
    if b != 0:
        return a / b
    else:
        return "Error no se puede dividir entre cero"

# Solicitar números y operación al usuario
a = float(input("ingrese el primer numero: "))
b = float(input("ingrese el segundo numero: "))

operacion = input("Ingresa la operacion (+, -, *, /,):  ")

# Realizar la operación según la opción elegida
if operacion == "+":
    resultado = suma(a,b)
elif operacion == "-":
    resultado = resta(a,b)
elif operacion == "*":
    resultado = multi(a,b)
elif operacion == "/":
    resultado = division(a,b)
else:
    resultado = "Operacion invalidad"

# Mostrar el resultado
print ("el resultado es: ", resultado)


