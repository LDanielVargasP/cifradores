import numpy as np

alfabeto = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

validacion = True
validacion2 = True

if validacion:
    mensaje = input("\nIngrese el mensaje (debe tener 6 letras y en MAYUSCULAS): ")

    if validacion and len(mensaje) != 6:
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
    


if validacion:
    print("\nResultado del criptograma: " + MetodoHillEncryptar(alfabeto, mensaje))
    validacion = False
