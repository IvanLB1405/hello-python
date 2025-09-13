#01
set1 = {1,2,3,4,5}
print(set1)

#02
set1.add(6)
print(set1)

#03
#No se pueden añadir duplicados a un set, no los permite el lenguaje

#04
print(3 in set1)

#05
set1.remove(4)
print(set1)

#06
set1.clear()
print(len(set1))

#07
set2 = {"Manzana", "naranja", "platano"}
list2 = list(set2)
print(list2[0])

#08
set3 = {1,2,3}
set4 = {4,5,6}
set5 = set3.union(set4)
print(set5)

#09
set6 = {1,2,3,4}
set7 = {3,4,5,6}
print(set6.difference(set7))

#10
my_set = {1,2,3}
del my_set
print(my_set)

