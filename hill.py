frase = str(input("Coloque la frase a cifrar en mayusculas: "))
print(f'frase {frase}')


diccionario_encriptacion = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9,
                            'K': 10, 'L': 11, 'M': 12, 'N': 13, 'Ñ': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18,
                            'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26, ' ': 27}

matrix = []

for i in range(0, len(frase)):
            matrix.append(diccionario_encriptacion[frase[i]])


print(f'{matrix}')