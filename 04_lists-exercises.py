#01
mylist1 = [1,2,3,4,5]
print(mylist1)

#02
mylist2 = [10,20,30,40,50]
print(mylist2[2])

#03
mylist1.append(6)
print(mylist1)

#04
mylist2.insert(1,15)
print(mylist2)

#05
mylist3=[10,20,30,30,40,50]
mylist3.remove(30)
print(mylist3)

#06
number_popped = mylist1.pop()
print(number_popped)
print(mylist1)

#07
mylist4 = [100,200,300,400,500]
print(mylist4)
mylist4.reverse()
print(mylist4)

#08
mylist5 = [3,1,4,2,5]
print(mylist5)
mylist5.sort()
print(mylist5)

#09
mylist6 = [1,2,3]
mylist7 = [4,5,6]
mylist8 = mylist6+mylist7
print(mylist8)

#10
mylist9 = mylist2[0:2]
print(mylist9)