#01
num = 0
if num < 0:
    print("El numero es negativo")
elif num == 0:
    print("El numero es cero")
else:
    print("El numero es positivo")
#02
"""
age = int(input("Ingresa tu edad"))
if age >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")
"""
#03
string = "asd"
if string:
    print("La cadena NO esta vacia")
else:
    print("La cadena esta vacia")

#04
"""
num1 = int(input("Ingresa un numero"))
num2 = int(input("Ingresa un numero"))
if num1 > num2:
    print("el primero es mayor")
elif num1 == num2:
    print("Son iguales")
else:
    print("El segundo es mayor")
"""
#05
num = 5
if num % 3 == 0 and num % 5 == 0:
    print(f"El numero {num} es divisible entre 3 y 5")
else:
    print(f"El numero {num} no es divisible entre 3 y 5")


#06
"""
num = int(input("Ingresa un numero"))
if num % 2 == 0:
    print(f"El numero {num} es par")
else:
    print("Es impar")
"""
#07
age = 1
if age >= 18:
    print("Puedes votar")
elif age == 16 or age == 17:
    print("Puedes votar con autorizacion de tus padres")
else:
    print("No puedes votar")

#08
"""
passwd = "asd"
user_passwd = input("Ingresa tu contraseña").lower()
if user_passwd == passwd:
    print("Login correcto")
else:
    print("Contraseña incorrecta")
"""
#09
num = 10
if num >= 10 and num <= 20:
    print("El numero esta entre 10 y 20")
else:
    print("El numero no esta en rango")

#10
semaforo = input("Introduce un color (rojo, amarillo, verde)").lower()
if semaforo == "rojo":
    print("No puedes pasar")
elif semaforo == "amarillo":
    print("Ten cuidao")
elif semaforo == "verde":
    print("Puedes pasar")
else:
    print("No es un color valido")
