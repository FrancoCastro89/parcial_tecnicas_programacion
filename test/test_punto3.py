import punto3
import unittest

class punto3Test(unittest.TestCase):

    def testRecibeUnPartidoAnuladoYNoRetornaNigunGanador(self):

        # ARRANGE
        tupla = []

        # ACT
        Resultado = punto3.calcularGanador(tupla)

        # ASSERT
        self.assertEqual(Resultado, "")

    def testRecibeUnPartidoYRetornaElGanadorDelPartido(self):

        # ARRANGE
        tupla = [("a", 1, "b", 0)]

        # ACT
        Resultado = punto3.calcularGanador(tupla)

        # ASSERT
        self.assertEqual(Resultado, "a")

    def testRecibeTresPartidosYRetornaElEquipoConMasGoles(self):

        # ARRANGE
        tupla = [("a", 1, "b", 0), ("a", 1, "c", 2), ("c", 3, "b", 0)]

        # ACT
        Resultado = punto3.calcularGanador(tupla)

        # ASSERT
        self.assertEqual(Resultado, "c")

    def testRecibeTresPartidosYRetornaElEquipoQueJugoMasPartidos(self):

        # ARRANGE
        tupla = [("Boca", 1, "Belgrano", 1), ("Boca", 1, "Almagro", 1), ("Almagro", 1, "Belgrano", 1)]

        # ACT
        Resultado = punto3.calcularGanador(tupla)

        # ASSERT
        self.assertEqual(Resultado, "Almagro")


    def testRecibeCuatroPartidosYRetornaElEquipoQueTieneMasGolesYQueJugoMasPartidos(self):
        # ARRANGE
        tupla = [("a", 1, "b", -2), ("a", 1, "c", 1), ("c", 1, "b", 1), ("d", 1, "a", 9)]

        # ACT
        Resultado = punto3.calcularGanador(tupla)

        # ASSERT
        self.assertEqual(Resultado, "a")

