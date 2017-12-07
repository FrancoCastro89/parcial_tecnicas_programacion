def devuelveUnaLisDeTodasLasRotacionesPosibles(palabra):
    """

    :param palabra: recibe un str

    :return: regresa una lista de todas las posibles rotaciones de ese str

    """

    lista = []

    palabravacia = palabra.split(" ")
    for recorePalabra in range(len(palabravacia)):
        if palabravacia[recorePalabra] == '':
            return lista

    if type(palabra) == str:
        listapalabra = list(palabra)
        lista.append(listapalabra)
        for x in range(len(palabra)):
            p = lista[x]
            lista1 = []
            for y in range(1, len(palabra)):
                lista1.append(p[y])
            lista1.append(p[0])
            lista.append(lista1)
        cosas = []
        for x in range(len(lista) - 1):
            cosas.append(''.join(lista[x]))
        return cosas
    else:
        return lista
