#01 #02
class Animal:
    def __init__(self, specie):
        self.specie = specie
    def make_sound(self):
        if self.specie.casefold() == "Dog".casefold():
            print("guau")
        elif self.specie.casefold() == "Cat".casefold():
            print("Miau")
        else:
            print("Sonido generico")

var1 = Animal("DOG")
var1.make_sound()

#03 #04
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.__speed = 0

    def get_speed(self):
        return self.__speed
    
    def accelerate(self):
        self.__speed += 10
    def brake(self):
        if self.__speed <= 0:
            print("Puedes frenar pero ya estas parado")
        else:
            self.__speed -= 10

car1 = Car("Renault", "Clio")
car1.accelerate()
print(car1.get_speed())
car1.brake()
print(car1.get_speed())
car1.brake()
        
#05
class Book:
    def __init__(self):
        self.title = ""
        self.__author = ""

    def get_author(self):
        return self.__author
    
    def set_title(self, title):
        self.title = title


#06
class Estudiante:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.notas = []

    def set_notas(self, notas):
        self.notas = notas

    def nota_media(self):
        sum = 0
        for nota in self.notas:
            sum += nota
        return sum / len(self.notas)

estudiante1 = Estudiante("Ivan", "Fernandez")
estudiante1.set_notas([1,2,3,4,5,6,7,8,9])
print(estudiante1.nota_media())

#07
class BankAccount:
    def __init__(self):
        self.__owner = "Ivan"
        self.__balance = 0

    def deposit(self, amount):
        self.__balance += amount

    def withdrawal(self, amount):
        if self.__balance < amount:
            print("No puedes retirar tanto dinero")
        else:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

myinvestor = BankAccount()
myinvestor.deposit(100)
print(myinvestor.get_balance())
myinvestor.withdrawal(100)
print(myinvestor.get_balance())

#08
class Point:
    def __init__(self, point1, point2):
        self.x = point1
        self.y = point2

    #Entiende que other_point será otro point con atributos x e y devuelve con teorema de pitagoras la distancia.Hacer ** 0.5 es == que hacer raiz cuadrada
    def calculate_distance(self, other_point):
        distance_x = abs(self.x - other_point.x)
        distance_y = abs(self.y - other_point.y)
        return (distance_x ** 2 + distance_y **2) ** 0.5
    

point1 = Point(3,4)
print(point1.calculate_distance(Point(0,0)))

#09
class Employee:
    def __init__(self, name, hourly_wage, hours_worked):
        self.__name = name
        self.__hourly_wage = hourly_wage
        self.__hours_worked = hours_worked

    def get_hourly_wage(self):
        return self.__hourly_wage
    

    def get_hours_worked(self):
        return self.__hours_worked
        
    def nomina(self):
        return self.__hourly_wage * self.__hours_worked
    
employee1 = Employee("Ivan", 30, 160)
print(employee1.nomina())

#10
class Store:
    def __init__(self, inventory):
        self.__inventory = inventory

    def mostrar_productos(self):
        for product in self.__inventory:
            print(product)

    def add_producto(self, producto):
        self.__inventory.append(producto)

mitienda = Store(["Peras", "Manzanas", "Galletas"])
mitienda.mostrar_productos()
mitienda.add_producto("Platanos")
mitienda.mostrar_productos()