'''
Integrantes:
Luis Daniel Vargas Peña
Jesus Israel Baltazar Peña
Francisco Obledo Garcia
'''
import os
import random

            #variables Playfair
#-----------------------------------------------------
        #  0    1    2    3    4    5       llave
matPC = [['.', 'l', 'u', 'i', 's', 'd'], # 0
        ['a', 'n', 'í', 'e', 'b', 'v'], # 1
        ['á', 'r', 'g', 'c', 'f', 'p'], # 2
        ['é', 'ñ', 'h', 'j', 'k', 'm'], # 3
        ['o', 'ó', 'q', 't', 'ú', 'ü'], # 4
        [',', 'w', 'x', 'y', 'z', ' '], # 5
        ]

lista = ['.', ',', ' ']
textoLC = textoLD = ''
textoC = ''
textoD = ''
            #funciones Playfair
#-----------------------------------------------------
def ordenar(i, p, aux, opc): #acomoda la palabra al formato correcto para usar playfair
    if opc:
        l = len(p)
        if i < l:
            if p[i-1] == p[i]:
                aux += p[i-1]
                aux += random.choice(lista)
                global textoLC
                textoLC = aux
                for j in range(i, len(p), 1):
                    textoLC += p[j]
                ordenar(i+2, textoLC, aux, 1)
            else:
                aux += p[i-1]
                aux += p[i]
                ordenar(i+2, p, aux, 1)
        else:
            textoLC = p
            pass
    else:
        l = len(p)
        if i < l:
            if p[i-1] == p[i]:
                aux += p[i-1]
                aux += random.choice(lista)
                global textoLD
                textoLD = aux
                for j in range(i, len(p), 1):
                    textoLD += p[j]
                ordenar(i+2, textoLD, aux, 0)
            else:
                aux += p[i-1]
                aux += p[i]
                ordenar(i+2, p, aux, 0)
        else:
            textoLD = p
            pass

def cifrarplayfair(p):
    global textoC
    textoC = ''
    x = y = x2 = y2 = 0
    for i in range(0, len(p), 2):
        for fila in range(6):
            for columna in range(6):
                if matPC[fila][columna] == p[i]:
                    x = columna
                    y = fila
                    break
        for fila in range(6):
            for columna in range(6):
                if matPC[fila][columna] == p[i+1]:
                    x2 = columna
                    y2 = fila
                    break
        if x < x2 and y > y2: #nu
            textoC += matPC[y2][x]
            textoC += matPC[y][x2]
        elif x > x2 and y < y2: #un
            textoC += matPC[y2][x]
            textoC += matPC[y][x2]
        elif x == x2:
            textoC += matPC[(y+1) % 6][x2]
            textoC += matPC[(y2+1) % 6][x]
        elif y == y2:
            textoC += matPC[y2][(x+1) % 6]
            textoC += matPC[y][(x2+1) % 6]
        else:
            textoC += matPC[y][x2]
            textoC += matPC[y2][x]

def descifrarplayfair(p):
    global textoD
    textoD = ''
    x = y = x2 = y2 = 0
    for i in range(0, len(p), 2):
        for fila in range(6):
            for columna in range(6):
                if matPC[fila][columna] == p[i]:
                    x = columna
                    y = fila
                    break
        for fila in range(6):
            for columna in range(6):
                if matPC[fila][columna] == p[i+1]:
                    x2 = columna
                    y2 = fila
                    break
        if x < x2 and y > y2: #nu
            textoD += matPC[y][x2]
            textoD += matPC[y2][x]
        elif x > x2 and y < y2: #un
            textoD += matPC[y][x2]
            textoD += matPC[y2][x]
        elif x == x2:
            textoD += matPC[(y-1) % 6][x2]
            textoD += matPC[(y2-1) % 6][x]
        elif y == y2:
            textoD += matPC[y2][(x-1) % 6]
            textoD += matPC[y][(x2-1) % 6]
        else:
            textoD += matPC[y2][x]
            textoD += matPC[y][x2]

def menuPlayfair():
    print('''
            Cifrado Playfair

    0) Salir
    1) Encriptar
    2) Desencriptar
    ''')
    y = input('Elija una opcion: ')

    if y == '0':
        return
    elif y == '1':
        os.system('cls')
        print('Funcion Encriptar')
        palabra = input("Escribe la palabra a encriptar: \n")
        palabra = palabra.replace(" ", "")
        palabra = palabra.lower()
        limite = len(palabra)
        if limite > 1:
            ordenar(1, palabra, '', 1)
        else:
            global textoLC
            textoLC = palabra
        if len(textoLC) % 2 == 1:
            textoLC = textoLC + random.choice(lista)
        print('Tu palabra se ha acomodado al formato correcto \n')
        print(textoLC)
        cifrarplayfair(textoLC)
        print(textoC)
        menuPlayfair()
    elif y == '2':
        os.system('cls')
        print('Funcion Desencriptar')
        palabra = input("Escribe la palabra a desencriptar: \n")
        palabra = palabra.replace(" ", "")
        palabra = palabra.lower()
        limite = len(palabra)
        if limite > 1:
            ordenar(1, palabra, '', 0)
        else:
            global textoLD
            textoLD = palabra
        if len(textoLD) % 2 == 1:
            textoLD = textoLD + random.choice(lista)
        print('Tu palabra se ha acomodado al formato correcto \n')
        print(textoLD)
        descifrarplayfair(textoLD)
        print(textoD)
        menuPlayfair()
    else:
        os.system('cls')
        print('Opcion NO valida intente de nuevo')
        menuPlayfair()

#-----------------------------------------------------
def menuOTP():
    print('''
            Cifrado OTP

    0) Salir
    1) Encriptar
    2) Desencriptar
    ''')
    y = input('Elija una opcion: ')

    if y == '0':
        return
    elif y == '1':
        os.system('cls')
        print('Funcion Encriptar')
        menuOTP()
    elif y == '2':
        os.system('cls')
        print('Funcion Desencriptar')
        menuOTP()
    else:
        os.system('cls')
        print('Opcion NO valida intente de nuevo')
        menuOTP()


if __name__ == '__main__':
    x = 1
    while x == 1:
        os.system('cls')
        print('''
            Bienvenido
        
        0) Salir
        1) Cifrado de Playfair
        2) Cifrado de Hill
        3) Cifrado OTP
        ''')
        y = input('Elija una opcion: ')
        if y == '0':
            x = 0
        elif y == '1':
            os.system('cls')
            print('Cifrado de Playfair')
            menuPlayfair()
        elif y == '2':
            os.system('cls')
            print('Cifrado de Hill')
        elif y == '3':
            os.system('cls')
            menuOTP()
        else:
            os.system('cls')
            print('Opcion NO valida intente de nuevo')
        