#!/usr/bin/env python3

def formingMagicSquare(s):
    # Write your code here
    suma = 15
    suma_row = 0
    suma_col = 0
    lista_sumas_row=[]
    lista_sumas_cols = []
    for a in range(3):
        for i,val in enumerate(s):
            for j, val2 in enumerate(val):
                suma_row +=val2
            lista_sumas_row.append(suma_row)
            suma_col +=val[i]
            suma_row=0
        lista_sumas_cols.append(suma_col)
        suma_col=0
    print(lista_sumas_row)
    print(lista_sumas_cols)

formingMagicSquare([[4, 9, 2], [3, 5, 7], [8, 1, 6]])    