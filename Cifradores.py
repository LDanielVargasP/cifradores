import numpy as np

alfabeto = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "Ñ", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
alfabetoIngles = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

validacion = True

alfabetoDeseado = (input("\nIngles \nCastellano \n\n Introduzca el alfabeto que usara: "))

if alfabetoDeseado == "INGLES":
    alfabetoSeleccionadao = alfabetoIngles
elif alfabetoDeseado == "CASTELLANO":
    alfabetoSeleccionado = alfabeto
else:
    print("Ingrese el alfabeto que desee: ")
    validacion = False

if validacion:
    llavek = input("\nIngrese la llave (La llave debe de tener 9 letras y MAYUSCULAS): ")
    if len(llavek) != 9:
        print("la llave debe de tener 9 caracteres")
        validacion = False
    else:
        mensaje = input("\nIngrese el mensaje (debe tener 6 letras y en MAYUSCULAS): ")
    if validacion and len(mensaje) != 6:
        print("El mensaje debe de tener 6 caracteres")
        validacion = False

def MetodoHill(alfabeto, llave, mensaje):
    #Declaracion de las matrices
    K = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
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

    # insertar la llave en la matriz K
    letrak = 0
    for k in range(0, 3):
        for l in range(0, 3):
            for j in range(0, len(alfabeto)):
                if llave[letrak] == alfabeto[j]:
                    K[k][l] = j
                    break
            letrak += 1
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
    criptograma += " "

    for i in range(0, 3):
        for j in range(0, len(alfabeto)):
            if y[i][0] == j:
                criptograma += alfabeto[j]

    return criptograma


if validacion:
    print("\nResultado del criptograma: " + MetodoHill(alfabetoSeleccionado, llavek, mensaje))
    validacion = False
