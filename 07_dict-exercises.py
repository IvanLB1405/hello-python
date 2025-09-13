#01
dict1 = {
    "name": "Ivan",
    "age": 30,
    "country": "Spain",
}
print(dict1)

#02
print(dict1["name"])
#03
dict1["Job"] = "Programador"
print(dict1)
#04
dict1["age"] = 38
print(dict1)

#05
del dict1["country"]
print(dict1)
#06
dict2 = {
    1:1,
    2:4,
    3:9,
    4:16,
    5:25,
}
print(dict2)
#07
print("age" in dict1.keys())
#08
print(dict1.keys())
#09
list1 = list(dict1.keys())
print(list1)
#10
my_new_dict = dict.fromkeys(list1, "Desconocido")
print(my_new_dict)