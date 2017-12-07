import punto3
import unittest

class punto3Test(unittest.TestCase):

    def testCalculandoGanador1(self):
        # ARRANGE
        tupla = []

        # ACT
        Resultado = punto3.calcularGanador(tupla)

        # ASSERT
        self.assertEqual(Resultado, "")

    def testCalculandoGanador2(self):

        self.assertEqual(punto3.calcularGanador([("a", 1, "b", 0)]), "a")

    def testCalculandoGanador3(self):

        self.assertEqual(punto3.calcularGanador([("a", 1, "b", 0), ("a", 1, "c", 2), ("c", 3, "b", 0)]), "c")

    def testCalculandoGanador4(self):

        self.assertEqual(punto3.calcularGanador([("Boca", 1, "Belgrano", 1), ("Boca", 1, "Almagro", 1), ("Almagro", 1, "Belgrano", 1)]), "Almagro")

    def testCalculandoGanador(self):

        self.assertEqual(punto3.calcularGanador([("a", 1, "b", -2), ("a", 1, "c", 1), ("c", 1, "b", 1), ("d", 1, "a", 9)]), "a")

