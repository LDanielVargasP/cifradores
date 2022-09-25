'''
Integrantes:
Luis Daniel Vargas Peña
Jesus Israel Baltazar Peña
Francisco Obledo Garcia
'''
import os


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
    elif y == '2':
        os.system('cls')
        print('Cifrado de Hill')
    elif y == '3':
        os.system('cls')
        menuOTP()
    else:
        os.system('cls')
        print('Opcion NO valida intente de nuevo')
    