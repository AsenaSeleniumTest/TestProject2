import sys

a =[1,3,8,9,5,"7",4,2,6]
b = [1,2,3,4,5,6,7,8,9]
print(a)      
a.extend(b) # a = a + b  
a.pop()
print(a)  
print(a.index(5)) # 2      
print(sys.getsizeof(a)) # 104
c = a
print(id(a))
print(id(c)) # 140706803200064