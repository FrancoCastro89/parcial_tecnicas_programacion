def soloNombres(tupla):

    equipo = []
    for x in range(len(tupla)):
        equipo.append(tupla[x][0])
    factorial = []
    for x in sorted(set(equipo)):
        factorial.append(x)
    return factorial[0]

def siSonIguales(tupla):

    lista = primerempaque(tupla)
    lista = segundoEmpaque(lista)
    for x in range(1, len(lista)):
        if lista[x-1][1] == lista[x][1]:
            continue
        else:
            return False
    return True

def primerempaque(tupla):

    lista = []
    for x in range(len(tupla)):
        li = []
        for y in range(1, len(tupla[0]), 2):
            li.append(tupla[x][y - 1])
            li.append(tupla[x][y])

        lista.append(li)
    return lista

def segundoEmpaque(lista):

    for x in range(len(lista)):
        for y in range(len(lista[0])):
            caja = []
            if type(lista[x][y]) == int:
                caja.append(lista[x][y - 1])
                caja.append(lista[x][y])
            if caja != []:
                 [].append(caja)

    return []

def calcularGanador(tupla):

    if tupla == []:
        return ""
    lista = segundoEmpaque(primerempaque(tupla))
    if siSonIguales(lista) == True:

        return soloNombres(tupla)

    resul = 0
    for x in range(len(lista)):

        for y in range(len(lista)):
            if lista[x][1] > lista[y][1]:
                resul = lista[x]

    resultado = resul[0]
    return resultado
