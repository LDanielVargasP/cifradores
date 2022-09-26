from ast import match_case
import numpy as np

alfabeto = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

validacion = False
validacion2 = False

opcion = input("Que desea hacer:\nEncryptar = 1\nDesencriptar = 2\n ")

match opcion:
    case "1":
        validacion = True
        if validacion:
            mensaje = input("\nIngrese el mensaje (debe tener 6 letras y en MAYUSCULAS): ")
        if validacion and len(mensaje) != 6:
            print("El mensaje debe de tener 6 caracteres")
            validacion = False


    case "2":
        validacion2 = True
        if validacion2:
            mensajeEncryptado = input("\nIngrese el mensaje a decifrar(debe tener 6 letras y en MAYUSCULAS): ")

        if validacion and len(mensajeEncryptado) != 6:
            print("El mensaje debe de tener 6 caracteres")
            validacion = False

def MetodoHillEncryptar(alfabeto, mensaje):
    #Declaracion de las matrices
    K = [
        [1, 0, 1],
        [0, 2, 1],
        [1, 5, 4],
    ]
    M1 = [
        [0],
        [0],
        [0]
    ]
    M2 = [
        [0],
        [0],
        [0]
    ]
    x = [
        [0],
        [0],
        [0]
    ]
    y = [
        [0],
        [0],
        [0]
    ]

    
    # insertar las primeras tres letras  del mensaje en la matriz M1
    letraMensaje = 0
    for i in range(0, 3):
        for j in range(0, len(alfabeto)):
            if mensaje[letraMensaje] == alfabeto[j]:
                M1[i][0] = j
                break
        letraMensaje += 1

    for i in range(0, 3):
        for j in range(0, len(alfabeto)):
            if mensaje[letraMensaje] == alfabeto[j]:
                M2[i][0] = j
                break
        letraMensaje += 1

    #imprimir las matrices
    print("Estas seran las matrices que se usaran: ")

    print("matriz K: ")
    for line in K:
        print(' '.join(map(str, line)))
    print("\n")

    print("Matriz M1")
    for line in M1:
        print(' '.join(map(str, line)))
    print("\n")

    print("Matriz M2")
    for line in M2:
        print(' '.join(map(str, line)))
    print("\n")

    # Se multiplican las natrices con la libreria numpy
    x = np.dot(K, M1)
    y = np.dot(K, M2)

    # Variable para obtener la cantidad de letras en el abecedario
    tamanoAbecedario = len(alfabeto)

    # Ciclo para obtner el resultado de los modulos
    for i in range(0, 3):
        x[i][0] = x[i][0] % tamanoAbecedario
        y[i][0] = y[i][0] % tamanoAbecedario

    # ciclos para obtener el criptograma
    criptograma = ""
    for i in range(0, 3):
        for j in range (0, len(alfabeto)):
            if x[i][0] == j:
                criptograma += alfabeto[j]
    criptograma += ""

    for i in range(0, 3):
        for j in range(0, len(alfabeto)):
            if y[i][0] == j:
                criptograma += alfabeto[j]

    return criptograma

def MetodoHillDesencryptar(alfabeto, mensaje2):
    K = [
        [3, 5, -2],
        [1, 3, -1],
        [-2, -5, 2],
    ]
    M1 = [
        [0],
        [0],
        [0]
    ]
    M2 = [
        [0],
        [0],
        [0]
    ]
    x = [
        [0],
        [0],
        [0]
    ]
    y = [
        [0],
        [0],
        [0]
    ]

    
    # insertar las primeras tres letras  del mensaje en la matriz M1
    letraMensaje = 0
    for i in range(0, 3):
        for j in range(0, len(alfabeto)):
            if mensajeEncryptado[letraMensaje] == alfabeto[j]:
                M1[i][0] = j
                break
        letraMensaje += 1

    for i in range(0, 3):
        for j in range(0, len(alfabeto)):
            if mensajeEncryptado[letraMensaje] == alfabeto[j]:
                M2[i][0] = j
                break
        letraMensaje += 1

    #imprimir las matrices
    print("Estas seran las matrices que se usaran: ")

    print("matriz K: ")
    for line in K:
        print(' '.join(map(str, line)))
    print("\n")

    print("Matriz M1")
    for line in M1:
        print(' '.join(map(str, line)))
    print("\n")

    print("Matriz M2")
    for line in M2:
        print(' '.join(map(str, line)))
    print("\n")

    # Se multiplican las natrices con la libreria numpy
    x = np.dot(K, M1)
    y = np.dot(K, M2)

    # Variable para obtener la cantidad de letras en el abecedario
    tamanoAbecedario = len(alfabeto)

    # Ciclo para obtner el resultado de los modulos
    for i in range(0, 3):
        x[i][0] = x[i][0] % tamanoAbecedario
        y[i][0] = y[i][0] % tamanoAbecedario

    # ciclos para obtener el criptograma
    criptograma = ""
    for i in range(0, 3):
        for j in range (0, len(alfabeto)):
            if x[i][0] == j:
                criptograma += alfabeto[j]
    criptograma += ""

    for i in range(0, 3):
        for j in range(0, len(alfabeto)):
            if y[i][0] == j:
                criptograma += alfabeto[j]

    return criptograma
    


if validacion:
    print("\nResultado del criptograma: " + MetodoHillEncryptar(alfabeto, mensaje))
    validacion = False
if validacion2:
    print("\nResultado de desencriptacion: " + MetodoHillDesencryptar(alfabeto, mensajeEncryptado))
    validacion = False
'''
Integrantes:
Luis Daniel Vargas Peña
Jesus Israel Baltazar Peña
Francisco Obledo Garcia
'''
import os
import random 
from random import randint

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


def verificarLenguaje(entrada):

    print('La frase es: '+entrada)
    lgValido = 'abcdefghijklmnñopqrstuvwxyzáéíóúü., '

    for x in entrada: #Se verifica que sea la frase parte del lenguaje valido
        if lgValido.find(x) == -1:
            return False

    return True



def CifradoOneTimePad(frase):  #Crea la llave del tamanio de la frase
    
    abecedario = 'abcdefghijklmnñopqrstuvwxyzáéíóúü'
    llave = ''
    msjCifrado = ''

    for x in range(len(frase)): #Hace numeros aleatorios y agrega a la llave segun el indice aleatorio del abecedarios
        
        k = randint(0,len(abecedario)-1)
        llave += abecedario[k]
    
    print('La llave es: '+llave)
    
    for x in range(len(frase)):
        if frase[x] == ' ' or frase[x] == '.' or frase[x] == ',': #Si tiene espacio punto o coma lo pasa directamente
            msjCifrado += frase[x]
            
        else:
            i = abecedario.find(frase[x]) + abecedario.find(llave[x]) #Hace la suma de los indices
            
            if i > (len(abecedario) - 1): #si es mayor que el abecedario los resta para poder empezar de 0 
                i = i - (len(abecedario) - 1) - 1
                msjCifrado += abecedario[i]
            else:
                msjCifrado += abecedario[i] #Si no pasa la letra correspondiente de la suma
            
    print('El mensaje cifrado es: '+msjCifrado)



def DesencriptarOneTimePad():
    abecedario = 'abcdefghijklmnñopqrstuvwxyzáéíóúü'
    msjDescrifrado = ''
    mensaje = input('Ingresa el mensaje a Desencriptar: ')
    if not verificarLenguaje(mensaje):
        print('Mensaje no valido')
        return
    llave = input('Ingrese la llave: ')
    if len(llave) < len(mensaje):
        print('Llave no valida')
        return

    for x in range(len(mensaje)):
        if mensaje[x] == ' ' or mensaje[x] == '.' or mensaje[x] == ',': #Si tiene espacio punto o coma lo pasa directamente
            msjDescrifrado += mensaje[x]
            
        else: 
            i = abecedario.find(mensaje[x]) - abecedario.find(llave[x]) #Hace la resta de los indices
            if i < 0: 
                i = len(abecedario) + i #Si es negativo vuelve a dar la vuelta al abecedario para no desbordarse
                msjDescrifrado += abecedario[i]
            else:
                msjDescrifrado += abecedario[i] #Si no pasa el la letra de acuerdo al indice
            
    print('El mensaje Descifrado es: '+msjDescrifrado)
    

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
        mensaje = input('Ingresa la frase: ').lower()
        if verificarLenguaje(mensaje):
            CifradoOneTimePad(mensaje)
        else:
            print('Mensaje no valido')
        menuOTP()
    elif y == '2':
        os.system('cls')
        DesencriptarOneTimePad()
        menuOTP()
    else:
        os.system('cls')
        print('Opcion NO valida intente de nuevo')
        menuOTP()

#----------------------------------------------------------
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
        
