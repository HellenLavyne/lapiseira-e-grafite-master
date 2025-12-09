import unittest

from src.dureza import Dureza
from src.grafite import Grafite
from src.lapiseira import Lapiseira


class TestLapiseira(unittest.TestCase):

    def testInicializacao(self):
        lapiseira = Lapiseira(0.5)
        self.assertEqual(0.5, lapiseira.getCalibre(),
                         "Ao criar uma lapiseira o seu calibre deve ser igual ao informado")
        self.assertIsNone(lapiseira.getGrafite(), "Ao criar uma lapiseira ela deve vir sem grafite [null]")

    def testInserirGrafiteCerto(self):
        lapiseira = Lapiseira(0.5)
        grafite = Grafite(0.5, Dureza.G_2B, 10)
        self.assertTrue(lapiseira.inserir(grafite),
                        "Deve ser possivel inserir grafites que tenham o mesmo calibre da lapiseira")

    def testInserirGrafiteCalibreMenor(self):
        lapiseira = Lapiseira(0.5)
        grafite = Grafite(0.3, Dureza.G_2B, 10)
        self.assertFalse(lapiseira.inserir(grafite),
                         "Não Deve ser possivel inserir grafites que tenham um calibre menor do que o da lapiseira")

    def testInserirGrafiteCalibreMaior(self):
        lapiseira = Lapiseira(0.5)
        grafite = Grafite(0.8, Dureza.G_2B, 10)
        self.assertFalse(lapiseira.inserir(grafite),
                         "Não Deve ser possivel inserir grafites que tenham um calibre maior do que o da lapiseira")

    def testInserirGrafiteEmUmLapiseiraCheia(self):
        lapiseira = Lapiseira(0.5)
        grafite = Grafite(0.5, Dureza.G_2B, 10)
        self.assertTrue(lapiseira.inserir(grafite),
                        "Deve ser possivel inserir grafites que tenham o mesmo calibre da lapiseira")
        self.assertFalse(lapiseira.inserir(grafite),
                         "Não deve ser possivel inserir um grafite se a lapiseira ja tiver um")

    def testRemoverGrafite(self):
        lapiseira = Lapiseira(0.5)
        grafite = Grafite(0.5, Dureza.G_2B, 10)
        lapiseira.inserir(grafite)
        self.assertTrue(lapiseira.remover(), "Deve ser possivel remover o grafite que esta na lapiseira")

    def testRemoverGrafiteNaoInserido(self):
        lapiseira = Lapiseira(0.5)
        self.assertFalse(lapiseira.remover(), "Nao deve ser possivel remover um grafite nao inserido")

    def testEscrevendoSemGrafite(self):
        lapiseira = Lapiseira(0.5)
        self.assertFalse(lapiseira.escrever(100), "Nao deve ser possivel escrever sem um grafite")

    def testEscrevendoComHB(self):
        lapiseira = Lapiseira(0.5)
        grafite = Grafite(0.5, Dureza.G_HB, 10)
        lapiseira.inserir(grafite)
        self.assertTrue(lapiseira.escrever(10),
                        "Com esse grafite inserido, deve ser possivel escrever ate 10 paginas")
        self.assertEqual(10, lapiseira.getFolhasEscritas(), "Esta lapiseira deve ter escrito 10 paginas")
        self.assertIsNone(lapiseira.getGrafite(), "Ao consumir todo o grafite, a lapiseira deve ficar vazia")

    def testEscrevendoCom2B(self):
        lapiseira = Lapiseira(0.5)
        grafite = Grafite(0.5, Dureza.G_2B, 10)
        lapiseira.inserir(grafite)
        self.assertTrue(lapiseira.escrever(5),
                        "Com esse grafite inserido, deve ser possivel escrever ate 5 paginas")
        self.assertEqual(5, lapiseira.getFolhasEscritas(), "Esta lapiseira deve ter escrito 5 paginas")
        self.assertIsNone(lapiseira.getGrafite(), "Ao consumir todo o grafite, a lapiseira deve ficar vazia")

    def testEscrevendoCom4B(self):
        lapiseira = Lapiseira(0.5)
        grafite = Grafite(0.5, Dureza.G_4B, 16)
        lapiseira.inserir(grafite)
        self.assertTrue(lapiseira.escrever(4),
                        "Com esse grafite inserido, deve ser possivel escrever ate 4 paginas")
        self.assertEqual(4, lapiseira.getFolhasEscritas(), "Esta lapiseira deve ter escrito 4 paginas")
        self.assertIsNone(lapiseira.getGrafite(), "Ao consumir todo o grafite, a lapiseira deve ficar vazia")

    def testEscrevendoCom6B(self):
        lapiseira = Lapiseira(0.5)
        grafite = Grafite(0.5, Dureza.G_6B, 12)
        lapiseira.inserir(grafite)
        self.assertTrue(lapiseira.escrever(2),
                        "Com esse grafite inserido, deve ser possivel escrever ate 2 paginas")
        self.assertEqual(2, lapiseira.getFolhasEscritas(), "Esta lapiseira deve ter escrito 2 paginas")
        self.assertIsNone(lapiseira.getGrafite(), "Ao consumir todo o grafite, a lapiseira deve ficar vazia")

    def testEscrevendoAteAcabar(self):
        lapiseira = Lapiseira(0.5)
        grafite = Grafite(0.5, Dureza.G_6B, 12)
        lapiseira.inserir(grafite)
        self.assertFalse(lapiseira.escrever(4),
                         "Com esse grafite inserido, deve ser possivel escrever ate 2 paginas")
        self.assertEqual(2, lapiseira.getFolhasEscritas(), "Esta lapiseira deve ter escrito 2 paginas")
        self.assertIsNone(lapiseira.getGrafite(), "Ao consumir todo o grafite, a lapiseira deve ficar vazia")

    def testEscrevendoVariasVezesAteAcabar(self):
        lapiseira = Lapiseira(0.5)
        grafite = Grafite(0.5, Dureza.G_2B, 12)
        lapiseira.inserir(grafite)
        lapiseira.escrever(4)
        lapiseira.escrever(5)
        self.assertEqual(6, lapiseira.getFolhasEscritas(), "O total de folhas escritas com esse grafite tem q ser 6")

    def testEscrevendoVariasVezesSemAcabarGrafite(self):
        lapiseira = Lapiseira(0.5)
        grafite = Grafite(0.5, Dureza.G_HB, 12)
        lapiseira.inserir(grafite)
        lapiseira.escrever(4)
        lapiseira.escrever(5)
        self.assertEqual(9, lapiseira.getFolhasEscritas(), "O total de folhas escritas com esse grafite tem q ser 9")

    def testTrocandoGrafiteAposEscrita(self):
        lapiseira = Lapiseira(0.5)
        grafite = Grafite(0.5, Dureza.G_HB, 12)
        lapiseira.inserir(grafite)
        lapiseira.escrever(4)
        lapiseira.remover()
        lapiseira.inserir(grafite)
        self.assertEqual(0, lapiseira.getFolhasEscritas(), "Ao trocar de grafite a contagem deve ser zerada")

    if __name__ == '__main__':
        unittest.main()