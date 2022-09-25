
from traceback import print_tb


frase = str(input("Coloque la frase a cifrar en mayusculas: "))
print(f'frase {frase}')


diccionario_encriptacion = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
                            'K': 10, 'L': 11, 'M': 12, 'N': 13, 'Ñ': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18,
                            'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26, ' ': 27}

#for i in range(0, len(frase)):
#            matrix.append(diccionario_encriptacion[frase[i]])

a = len(frase)
print(a)
matrix = [[6,17,26]]
llave = [[1,0,1], [0,2,5], [1,1,4]]

m3 = []
for i in range(len(matrix)):
    m3.append([])
    for j in range(len(llave[0])):
        m3[i].append(0)

for i in range(len(matrix)):
    for j in range(len(llave[0])):
        for k in range(len(matrix[0])):
            m3[i][j] += matrix[i][k] * llave[k][j] % 37
print(m3)


#for i in range(0, len(frase)):
#            matrix.append(diccionario_encriptacion[frase[i]])


#print(f'{matrix}')
