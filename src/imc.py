def evaluar(peso, estatura, edad):
    # TODO: Coloca aquí el código del ejercicio 8: Índice de masa corporal
    resultado=""
    IMC = peso / (estatura * estatura)
    if  edad<45 and IMC < 22.0:      resultado = "bajo"
    elif IMC >= 22.0 and edad < 45:  resultado = "medio"
    elif IMC < 22.0 and edad >= 45:  resultado = "medio"
    elif IMC >= 22.0 and edad >= 45: resultado = "alto"
    return resultado

if __name__ == '__main__':
    print("Peso:", end="")
    peso = int(input())
    print("Estatura:", end="")
    estatura = float(input())
    print("Edad:", end="")
    edad = int(input())
        
    respuesta = evaluar(peso, estatura, edad)
    print(respuesta)
    