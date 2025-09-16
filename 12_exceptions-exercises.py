#01
"""
var1 = int(input("Introduce un numero"))
var2 = int(input("Introduce un numero"))

try:
    print(var1/var2)
except ZeroDivisionError as e:
    print("Se ha producido un error, division por cero")
    print(e)
"""
#02
def convert_to_int(string):
    try:
        return int(string)
    except Exception as e:
        print("Ha ocurrido un error")
        print(e)

convert_to_int("Hola")

#03
def readfile(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError as e:
        print("No se ha encontrado el fichero")
        print(e)
readfile("/home/ivan/hola.txt")

#04
def operations(num1, num2):
    try:
        sum = num1 + num2
        substract = num1 - num2
        multiply = num1 * num2
        divide = num1 / num2
        print(sum, substract, multiply, divide)
    except Exception as e:
        print("Ha ocurrido un error")
        print(e)
    else:
        print("Ha llegado a final de operaciones")
    finally:
        print("Espero que este contento con el resultado")

operations(10, 0)

#05
def ask_age():
    try:
        age = int(input("Introduce tu edad"))
        if age <= 0:
            raise ValueError("La edad debe ser un numero entero positivo")
        return age
    except ValueError as e:
        print(f"Error: {e}")

#ask_age()

#06
def index_access(list1):
    try:
        print(list1[10])
    except IndexError as e:
        print(f"Error: {e}")

index_access([1, 2, 3, 4, 5])

#07
def exception_handlers():
    try:
       #
        #var2 = int("Hola me llamo Ivan")
        var3 = "Hola" + 1
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")
    except TypeError as e:
        print(f"Error: {e}")
        print(type(e))

exception_handlers()

#08
class InsufficientFundsError(Exception):
    pass

def transaction(amount):
    balance = 100
    try:
        if amount > balance:
            raise InsufficientFundsError("Saldo insuficiente para la transaccion")
        else:
            balance -= amount
            print(f"Transaccion realizada correctamente, nuevo balance {balance}")
    except InsufficientFundsError as e:
        print(f"Error: {e}")

transaction(190)

#09
def convert_list_to_integers(list1):
    try:
        for string in list1:
            var1 = int(string)
            print(var1)
    except ValueError as e:
        print(f"Error: {e}")
        print(type(e))
convert_list_to_integers([1,2.0,"Pepe", 3.0])

#10
def squared_root(num):
    try:
        if num < 0:
            raise ValueError("No puedo hacer raiz cuadrada de un numero negativo")
        else:
            return num ** 0.5
    except ValueError as e:
        print(f"Error: {e}")
        print(type(e))

print(squared_root(-2))