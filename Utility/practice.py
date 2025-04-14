def powers_of_2(n):
    power = 1
    for i in range(n):
        yield power
        power *= 2
 
 

for i in range(33):
    if i in powers_of_2(6):
        print(f"{i} is a power of 2")