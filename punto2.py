def vidaDelasposicionesDeLosBarcos(vida, posicion):

    siguiente = []
    for f in range(len(vida)):
        fila = []
        for c in range(len(vida[0])):
            fila.append(continuandoConCeldaSiguiente(vida, f, c, posicion))
        siguiente.append(fila)
    return siguiente

def continuandoConCeldaSiguiente(vida, f, c, posicion):

    for x in range(len(posicion)):

        fi = (posicion[x][0]) - 1
        co = (posicion[x][1]) - 1
        if f == fi and c == co:
            punto = '.'
            return punto
    return vida[f][c]


def juego(mapa,posicionesDeDisparosDePrueba):

    caja = []
    for x in range(1, len(mapa)):
        if len(mapa[x - 1]) != len(mapa[x]):
            return caja
    pet = []
    for recorreFila in range(len(vidaDelasposicionesDeLosBarcos(mapa, posicionesDeDisparosDePrueba))):
        li = ()
        for recorreColumna in range(len(vidaDelasposicionesDeLosBarcos(mapa, posicionesDeDisparosDePrueba)[0])):
            if vidaDelasposicionesDeLosBarcos(mapa, posicionesDeDisparosDePrueba)[recorreFila][recorreColumna] == 'b':
                li = (recorreFila + 1, recorreColumna + 1)
            if li != [] and len(li) == 2:
                pet.append(li)
                li = []
    return pet
