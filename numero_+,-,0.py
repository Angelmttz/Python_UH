#Determinar si el  numero ingresado por el usuario positivo, negativo o cero

numero = float(input("Ingresa el numero para decirte si es negativo o positivo: "))

if numero < 0:
    print(f"El numero: ", numero, "es negativo")

elif numero > 0:
    print(f"El numero: ", numero, "es positivo")

else:
    print(f"el numero que ingresaste es un cero")