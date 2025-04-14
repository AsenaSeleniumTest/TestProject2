
def countingValleys(steps, path):
    # Write your code here
    index_d = []
    count_valley = 0
    lista_estatus_contador = []
    count_up_down = 0
    for i in range(len(path)):
        if path[i] == "D":
            index_d.append(i)
            count_up_down -= 1
            lista_estatus_contador.append(count_up_down)
        else:
            count_up_down += 1                        
            lista_estatus_contador.append(count_up_down)
    if lista_estatus_contador[0] == -1:   
        count_valley += 1     
    for j in  range(len(lista_estatus_contador)-1):
        if lista_estatus_contador[j] == 0 and lista_estatus_contador[j+1] == -1:
            count_valley += 1
    print("contador: ", lista_estatus_contador)
    return count_valley

print(countingValleys(12, "DDUUDDUDUUUD"))    