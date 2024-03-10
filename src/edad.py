def evaluar(dia, mes, anno):
    # TODO: Coloca aquí el código del ejercicio 6: Edad
    from time import localtime
    t= localtime ()
    dia_act=t.tm_mday
    mes_act=t.tm_mon
    anno_act=t.tm_year
    edad=anno_act-anno
    if mes_act < mes or (mes_act == mes and dia_act < dia):
        edad -= 1
    return edad

if __name__ == '__main__':
    print("Ingrese su fecha de nacimiento")
    print("Día:", end="")
    dia = int(input())
    print("Mes:", end="")
    mes = int(input())
    print("Año:", end="")
    anno = int(input())
        
    respuesta = evaluar(dia, mes, anno)
    print(respuesta)
