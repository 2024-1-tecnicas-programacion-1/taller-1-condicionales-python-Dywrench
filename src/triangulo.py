def evaluar(a, b, c):
    # TODO: Coloca aquí el código del ejercicio 1: Set de tenis
    triangulo = ""
    if a + b <= c or b + c <= a or c + a <= b:
        triangulo = "No es un triángulo válido"
    elif a == b and b == c:
        triangulo = "El triángulo es equilátero"
    elif a == b or b == c or c == a:
        triangulo = "El triángulo es isósceles"
    else:
        triangulo = "El triángulo es escaleno"
    return triangulo

    

if __name__ == '__main__':
    print("a:", end="")
    a = float(input())
    print("b:", end="")
    b = float(input())
    print("c:", end="")
    c = float(input())
        
    respuesta = evaluar(a, b, c)
    print(respuesta)
