from random import randint


frase = input('Ingresa la frase: ')
print('La frase es: '+frase)


def cifrarOneTimePad(frase):
    
    abecedario = 'abcdefghijklmnñopqrstuvwxyzáéíóúü'
    llave = ''

    for x in range(len(frase)): #Crea la llave del tamanio de la frase
        if frase[x] == ' ':
            llave += ' ' 
            x=+1
        else:
            k = randint(0,len(abecedario)-1)
            llave += abecedario[k]
        

    print(llave)

cifrarOneTimePad(frase)


