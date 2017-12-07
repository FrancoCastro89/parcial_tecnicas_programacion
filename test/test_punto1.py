import punto1
import unittest


class Punto1Test(unittest.TestCase):

    def testNoRecibeNingunaLetraYRetornaUnaListaVacia(self):

        # ARRANGE
        palabra = ""
        # ACT
        resultado = punto1.devuelveUnaLisDeTodasLasRotacionesPosibles(palabra)
        # ASSERT
        self.assertEqual(resultado, [])

    def testRecibeEspacioEnBlancoYRetornaUnalistaVacia(self):

        # ARRANGE
        palabra = "     "
        # ACT
        resultado = punto1.devuelveUnaLisDeTodasLasRotacionesPosibles(palabra)
        # ASSERT
        self.assertEqual(resultado, [])


    def testRecibeUnaLetraYRetornaLaListaDeEsaLetra(self):

        # ARRANGE
        palabra = "a"
        # ACT
        resultado = punto1.devuelveUnaLisDeTodasLasRotacionesPosibles(palabra)
        # ASSERT
        self.assertEqual(resultado, ['a'])

    def testRecibeDosletrasYRetornaUnaListaDeLasRotacionesDeEsasLetras(self):

        # ARRANGE
        palabra = "ab"
        # ACT
        resultado = punto1.devuelveUnaLisDeTodasLasRotacionesPosibles(palabra)
        # ASSERT
        self.assertEqual(resultado, ['ab', 'ba'])


    def testRecibeUnaPalabraYRetornaUnaListaDeSusPosiblesRotaciones(self):

        # ARRANGE
        palabra = "paz"
        # ACT
        resultado = punto1.devuelveUnaLisDeTodasLasRotacionesPosibles(palabra)
        # ASSERT
        self.assertEqual(resultado, ['paz', 'azp', 'zpa'])


    def testRecibeDosLetrasUnEspacioYUnaLetraRetornaListaConLasRotaciones(self):

        # ARRANGE
        palabra = "so l"
        # ACT
        resultado = punto1.devuelveUnaLisDeTodasLasRotacionesPosibles(palabra)
        # ASSERT
        self.assertEqual(resultado, ['so l','o ls',' lso','lso '])

    def testRecibeUnaPalabraYRetornaUnaListaDeSusRotaciones(self):

        # ARRANGE
        palabra = "rotar"
        # ACT
        resultado = punto1.devuelveUnaLisDeTodasLasRotacionesPosibles(palabra)
        # ASSERT
        self.assertEqual(resultado, ['rotar','otarr','tarro','arrot','rrota'])
