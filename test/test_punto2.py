import punto1
import unittest


class Punto1Test(unittest.TestCase):

    def testdevuelveUnaLisDeTodasLasRotacionesPosiblesRecibeUnElementoNoValidoDeberiavolverUnalistaVacia(self):
        # ARRANGE
        palabra = ""
        # ACT
        resultado = punto1.devuelveUnaLisDeTodasLasRotacionesPosibles(palabra)
        # ASSERT
        self.assertEqual(resultado, [])

    def testdevuelveUnaLisDeTodasLasRotacionesPosiblesRecibeUnElementoNoValidoDeberiavolverUnalistaVacia(self):

        self.assertEqual(punto1.devuelveUnaLisDeTodasLasRotacionesPosibles("     "), [])

    def testdevuelveUnaLisDeTodasLasRotacionesPosiblesRecibeUnElementoNoValidoDeberiavolverUnalistaDeA(self):

        self.assertEqual(punto1.devuelveUnaLisDeTodasLasRotacionesPosibles("a"), ['a'])

    def testdevuelveUnaLisDeTodasLasRotacionesPosiblesRecibeUnElementoNoValidoDeberiavolverUnalistaDeAyB(self):

        self.assertEqual(punto1.devuelveUnaLisDeTodasLasRotacionesPosibles("ab"), ['ab','ba'])

    def testdevuelveUnaLisDeTodasLasRotacionesPosiblesRecibeUnElementoNoValidoDeberiavolverUnalistaDePaz(self):

        self.assertEqual(punto1.devuelveUnaLisDeTodasLasRotacionesPosibles("paz"), ['paz','azp','zpa'])

    def testdevuelveUnaLisDeTodasLasRotacionesPosiblesRecibeUnElementoNoValidoDeberiavolverUnalistaDeSo_l(self):

        self.assertEqual(punto1.devuelveUnaLisDeTodasLasRotacionesPosibles("so l"), ['so l','o ls',' lso','lso '])

    def testdevuelveUnaLisDeTodasLasRotacionesPosiblesRecibeUnElementoNoValidoDeberiavolverUnalistaDeRotar(self):

        self.assertEqual(punto1.devuelveUnaLisDeTodasLasRotacionesPosibles("rotar"), ['rotar','otarr','tarro','arrot','rrota'])
