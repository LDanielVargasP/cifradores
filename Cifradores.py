from random import randint

mensaje = input('Ingresa la frase: ').lower()

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
    

    

if verificarLenguaje(mensaje):
    CifradoOneTimePad(mensaje)
else:
    print('Mensaje no valido')

DesencriptarOneTimePad()
