from random import randint

frase = input('Ingresa la frase: ')
print('La frase es: '+frase)


def CifradoOneTimePad(frase):  #Crea la llave del tamanio de la frase
    
    #abecedario = 'abcdefghijklmnñopqrstuvwxyzáéíóúü'
    abecedario = 'abcdefghijklmnopqrstuvwxyz' #25 len regresa 26
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

def DesencriptarOneTimePad(mensaje):
    pass

CifradoOneTimePad(frase)


