#01
mytuple1 = (10,20,30,40,50)
print(mytuple1)

#02
mytuple2 = (100,200,300,400,500)
print(mytuple2[1])

#03
#No se pueden modificar elementos de una tupla

#04
mytuple3 = (1,2,3,3,4,5,3,)
print(mytuple3.count(3))

#05
mytuple4 = ("Java", "Python", "JavaScript", "Python")
print(mytuple4.index("Python"))

#06
mytuple5 = (1,2,3)
mytuple6 = (4,5,6)
print(mytuple5 + mytuple6)

#07
subtuple = mytuple1[1:3]
print(subtuple)

#08
mytuple7 = ("rojo", "verde", "azul")
print(mytuple7)
mylist_from_tuple = list(mytuple7)
mylist_from_tuple[1] = "Amarillo"
mytuple7 = tuple(mylist_from_tuple)
print(mytuple7)

#09 SE BORRA LA TUPLA ENTERA, NO HACE CLEAR
#del mytuple7
#print(mytuple7)

#10
mytuple8 = (100,)
print(mytuple8)
print(type(mytuple8))