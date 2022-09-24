from random import randint


frase = input('Ingresa la frase: ')
print('La frase es: '+frase)


def CifradoOneTimePad(frase):  #Crea la llave del tamanio de la frase
    
    #abecedario = 'abcdefghijklmnñopqrstuvwxyzáéíóúü'
    abecedario = 'abcdefghijklmnopqrstuvwxyz' #25
    llave = ''
    msjCifrado = ''

    for x in range(len(frase)): #Hace numeros aleatorios y agrega a la llave segun el indice aleatorio del abecedarios
        
        k = randint(0,len(abecedario)-1)
        llave += abecedario[k]
    
    print('La llave es: '+llave)
    for x in range(len(frase)):
        if frase[x] == ' ' or frase[x] == '.' or frase[x] == ',':
            msjCifrado += frase[x]
        else:
            i = abecedario.find(frase[x]) + abecedario.find(llave[x])
            if i > len(abecedario) - 1:
                i = i - (len(abecedario) - 1) 
                msjCifrado += abecedario[i]
            else:
                msjCifrado += abecedario[i]

    print('El mensaje cifrado es: '+msjCifrado)

CifradoOneTimePad(frase)


