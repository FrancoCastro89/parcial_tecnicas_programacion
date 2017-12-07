import punto2
import unittest


class Punto2Test(unittest.TestCase):

    def testJuegoRecibeMapaVacioyPuntosDeDisparosRetornaUnaListaVacia(self):

        #ARRANGE
        mapa = []
        posicionesDeDisparosDePrueba = [(1,1),(3,4),(1,3),(4,5)]

        #ACT
        resultado = punto2.juego(mapa, posicionesDeDisparosDePrueba)

        #ASSERT
        self.assertEqual(resultado, [])

    def testJuegoRecibeunMapaVacioyListaConDisparosyRetornaUnaListavacia(self):

        #ARRANGE
        mapa = [""]
        posicionesDeDisparosDePrueba = [(1, 1), (3, 4), (1, 3), (4, 5)]

        #ACT
        resultado = punto2.juego(mapa, posicionesDeDisparosDePrueba)

        #ASSERT
        self.assertEqual(resultado, [])


    def testJuegoMapaEnBlancoYListaConDisparosYRetornaListaVacia(self):

        #ARRANGE
        mapa = ["      "]
        posicionesDeDisparosDePrueba = [(1, 1), (3, 4), (1, 3), (4, 5)]

        #ACT
        resultado = punto2.juego(mapa, posicionesDeDisparosDePrueba)

        #ASSERT
        self.assertEqual(resultado, [])

    def testJuegoRecibeUnMapaDeTresPalabrasyPuntosDeDisparosYRetornaUnaLista(self):

        #ARRANGE
        mapa = ["soy NO valido"]
        posicionesDeDisparosDePrueba = [ (1, 1), (3, 4), (1, 3), (4, 5)]

        #ACT
        resultado = punto2.juego(mapa, posicionesDeDisparosDePrueba)

        #ASSERT
        self.assertEqual(resultado, [])

    def testJuegoRecibeMapaDePalabrasYPosicionesDeDisparosReltornaUnaListaVacia(self):

        #ARRANGE
        mapa = ["yo", "tambien", "soy", "invalido"]
        posicionesDeDisparoDePrueba = [(1, 1), (3, 4), (1, 3), (4, 5)]

        #ACT
        resultado = punto2.juego(mapa, posicionesDeDisparoDePrueba)

        #ASSERT
        self.assertEqual(resultado, [])

    def testJuegoMapaDeLasPosicionesdeLosBarcosYPosicionesDeDisparodePuebaRetornaUnaListaVacia(self):

        #ARRANGE
        mapa = ["b.b.","....","..bb","b.b"]
        posicinesDeDisparoDePrueba = [(1, 1), (3, 4), (1, 3), (4, 5)]

        #ACT
        resultado = punto2.juego(mapa, posicinesDeDisparoDePrueba)


        #ASSERT
        self.assertEqual(resultado, [])

    def testJuegoMapaDeLasPosicioensDeLosBarcosyPuntosDeDisparoRetornaLaPosicionesdeLosBarcosVivos(self):

        #ARRANGE
        mapa = ["b.b..","b...b",".....","....b"]
        posicionesDeDisparoDePrueba = [(1,1),(3,4),(1,3),(4,5)]

        #ACT
        resultado = punto2.juego(mapa, posicionesDeDisparoDePrueba)

        #ASSERT
        self.assertEqual(resultado, [(2,1),(2,5)])

    def testJuegoMapaDeBarcosypuntoDeDisparoRetornalaPosiciondeLosvarcosVivos(self):

        #ARRANGE
        mapa = ["b..","...","..b"]
        posicionesDeDisparoDePrueba = []

        #ACT
        resultado = punto2.juego(mapa, posicionesDeDisparoDePrueba)
        #ASSERT
        self.assertEqual(resultado, [(1,1),(3,3)])
