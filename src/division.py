def evaluar(dividendo, divisor):
    # TODO: Coloca aquí el código del ejercicio 3: Division
    cociente = dividendo/divisor 
    residuo = dividendo%divisor
    respuesta = ''
    if residuo == 0:
        respuesta = "La división es exacta. \n" \
                    "Cociente: " + str(cociente) + "\n" \
                    "Residuo: " + str(residuo)
    elif residuo != 0:  # Corregido: Se agrega la condición para elif
        respuesta = "La división no es exacta. \n" \
                    "Cociente: " + str(cociente) + "\n" \
                    "Residuo: " + str(residuo)
    
    return respuesta

if __name__ == '__main__':
    print("Dividendo:", end="")
    dividendo = int(input())
    print("Divisor:", end="")
    divisor = int(input())

    respuesta = evaluar(dividendo, divisor)
    print(respuesta)
