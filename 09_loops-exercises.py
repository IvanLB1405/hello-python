#01
num1 = 0
while num1 < 10:
    print(num1)
    num1 += 1

#02
list1 = [10,20,30,40,50]
for num in list1:
    print(num)

#03
num2 = 1
sum = 0
while num2 <= 100:
    sum += num2
    num2 += 1
print(sum)

#04
word = "Python"
for letter in word:
    print(letter)

#05
num3 = 1
while num3 <= 50:
    if num3 % 7 == 0:
        print(f"El primer numero encontrado es {num3}")
        break
    num3 += 1

#06
my_dict = {
    "name" : "Brais",
    "age" : 37,
    "country" : "Galicia"
}
for key in my_dict.keys():
    print(key)

#07
num4 = 0
while num4 <=20:
    if num4 % 2 == 0:
        print(num4)
    num4 +=1

#08
for num in range(10, 0, -1):
    print(num)

#09
list2 = [30,10,30,20,30,40]
conteo = 0
for number in list2:
    conteo = list2.count(30)
print(f"El numero 30 aparece {conteo} veces")

#10
list3 = ["Barbara", "Lucho", "Ivan", "Brais", "Pepe", "Juan"]
for name in list3:
    if name.casefold() == "brais".casefold():
        print("He encontrado a Brais")
        break
    else:
        print(f"{name} ha sido encontrado")