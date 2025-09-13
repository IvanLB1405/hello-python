#1 -> 
name = "Ivan"
age = 30
height = 1.81
print(name)
print(age)
print(height)

#2 -> 
age_to_int = str(age)
print("Tengo la siguiente edad:" , age_to_int)

# 3 ->
is_student = True
print("Eres estudiante?", is_student)

#4 ->
name_lenght = len("Ivan")
print(name_lenght)

#5 -> 
name1, surname, city = "Ivan", "Fernandez", "Aviles"
print(name1, surname, city)

#6 ->
#fav_color = input("Introduce tu color favorito")
#print(fav_color)

#7 -> 
fruit = "Manzana"
print(fruit)
fruit = "cereza"
print(fruit)

#8 -> 
price = 1.1
price_to_int = int(price)
print(price_to_int)

#9 -> 
address_len = len("Calle la habana")
print("La longitud en caracteres de la direccion proporcionada es:", address_len)

#10 -> no se pueden forzar tipos en python
phone : int = 1234556789
phone = "patata"
print(type(phone))