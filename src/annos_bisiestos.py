def evaluar(anno):
    # TODO: Coloca aquí el código del ejercicio 2: Años bisiestos
     anio_bisiesto = ''
     if anno%4==0 & (anno%100!=0 | anno%400==0):
           anio_bisiesto=" es bisiesto"
     else: anio_bisiesto = "No es bisiesto"      
     return anio_bisiesto
if __name__ == '__main__':
    print("Año:", end="")
    anno = int(input())

    respuesta = evaluar(anno)
    print(anno,respuesta)
