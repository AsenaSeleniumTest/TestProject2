import sys

a =[1,3,8,9,5,"7",4,2,6]
b = [1,2,3,4,5,6,7,8,9]
c = ("tigre","gato","perro","zebra","leon","Jaguar")
print(type(a))
a = tuple(a)
print(type(a))
print(type(c))
(felino, dog, zebra, *felino2) = c
print(f"Felino has: {felino}")
print(f"dog has : {dog}")
print(f"Zebra has : {zebra}")
print(f"felino2 has : {felino2}")
sumatupla1 = c*2
print(sumatupla1)
dict1={"100":"tigre", "20":"gato", "150":"Jaguar", "86":"lince", "34":"puma","10":"tigre"}
print(dict1)
for i in dict1.items():
    print(i[1],sep=" : ",end="",)
others = 0
for i in range(2):
    for j in range(2):
        if i != j:
            others += 1
else:
    others += 1
print(others)                    