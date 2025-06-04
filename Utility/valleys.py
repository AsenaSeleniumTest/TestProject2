#!/usr/bin/env python3

def display(number):
    """function to display umbers with #"""
    lista_numeros= list(str(number))
    print(len(lista_numeros))
    val = 0
    while val < len(lista_numeros):
        col_list=[[[] for i in range(0,3)]  for j in range(5)]
        if lista_numeros[val] == '1':
            for i,sublist in enumerate(col_list):
                for j, elem in enumerate(sublist):
                    if j == 2:
                        col_list[i][j] = "#"
                    else:
                        col_list[i][j] = ""
            print(col_list,end="\n")
        elif lista_numeros[val] == '2':
            for i, sublist in enumerate(col_list):
                for j, elem in enumerate(sublist):                    
                    if (i != 1 and i != 3) :
                        col_list[i][j] = "#"
                    elif j==2:
                        col_list[i][j] = "#"
                    else:
                        col_list[i][j] =""
            print(col_list,end="\n")
        elif lista_numeros[val] == '3':
            for i in range(5):
                for j in range(3):
                    if (i != 1 or i != 2):
                        col_list[i][j] = "#" 
                    elif i==2 and (j != 1 or j != 2 ):
                        col_list[i][j] = "#"
                    else:
                        col_list[i][j] = " "
                print(col_list,end="\n")
                        
        elif lista_numeros[val] == '4':
            for i in range(3):
                for j in range(5):                    
                    if (i != 0 or i != 1) and j != 1:
                        col_list[i][j] = "#"                                                
                    elif  (i == 3 or i == 4) and j!=2:
                        col_list[i][j] = "#"
                    else:
                        col_list[i][j] ="_"
                print(col_list,end="\n")         
        elif lista_numeros[val] == '5':
            for i in range(3):
                for j in range(5):
                    pass
                    
                         
        elif lista_numeros[val] == '6':
            for i in range(3):
                for j in range(5):
                    pass
                        
        elif lista_numeros[val] == '7':
            for i in range(3):
                for j in range(5):
                    pass
                        
        elif lista_numeros[val] == '8':
            for i in range(3):
                for j in range(5):
                    pass
                        
        elif lista_numeros[val] == '9':
            for i in range(3):
                for j in range(5):
                    pass
                        
        elif lista_numeros[val] == '0':
            for i in range(3):
                for j in range(5):
                    pass
                        
        else:
            raise TypeError("Invalid Value input, must be character between 0-9")
        val+=1
  

display("2")
