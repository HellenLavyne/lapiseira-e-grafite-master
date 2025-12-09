import unittest

from src.dureza import Dureza
from src.grafite import Grafite


class TestGrafite(unittest.TestCase):

    def testGrafiteHB(self):
        hb = Grafite(0.7, Dureza.G_HB, 10)
        self.assertEqual(1, hb.desgastePorFolha(), "O desgaste do Grafite HB deve ser 1")

    def testGrafite2B(self):
        g2b = Grafite(0.5, Dureza.G_2B, 80)
        self.assertEqual(2, g2b.desgastePorFolha(), "O desgaste do Grafite 2B deve ser 2")

    def testGrafite4B(self):
        g4b = Grafite(0.1, Dureza.G_4B, 80)
        self.assertEqual(4, g4b.desgastePorFolha(), "O desgaste do Grafite 4B deve ser 4")

    def testGrafite6B(self):
        g6b = Grafite(0.3, Dureza.G_6B, 80)
        self.assertEqual(6, g6b.desgastePorFolha(), "O desgaste do Grafite 6B deve ser 6")


if __name__ == '__main__':
    unittest.main()