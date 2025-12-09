from src.grafite import Grafite


class Lapiseira:

    def __init__(self, calibre:float):
        self.calibre = calibre
        self.grafite = None
        self.folhas_escritas = 0

    def inserir (self, grafite: Grafite):
        if self.grafite is not None:
            return False

        # Verificando o calibre
        if self.calibre != grafite.getCalibre():
            return False

        self.grafite = grafite
        self.folhas_escritas = 0
        return True

    def remover(self):
        if self.grafite is None:
            return False

        self.grafite = None
        self.folhas_escritas = 0
        return True

    def escrever(self, folhas: int):
        if self.grafite is None:
            return False

        desgaste_por_folha = self.grafite.desgastePorFolha()
        tamanho_atual = self.grafite.getTamanho()
        desgaste_total_solicitado = folhas * desgaste_por_folha

        if tamanho_atual >= desgaste_total_solicitado:
            novo_tamanho = tamanho_atual - desgaste_total_solicitado
            self.grafite.setTamanho(novo_tamanho)
            self.folhas_escritas += folhas
            if novo_tamanho == 0:
                self.grafite = None
            return True
        else:
            folhas_completas = tamanho_atual // desgaste_por_folha
            self.grafite.setTamanho(0)
            self.folhas_escritas += folhas_completas
            self.grafite = None
            return False

    def getGrafite(self):
        return self.grafite

    def getCalibre(self):
        return self.calibre

    def getFolhasEscritas(self):
        return self.folhas_escritas

    def toString(self):
        grafite_str = self.grafite.toString() if self.grafite else "null"
        return f"calibre: {self.calibre:.1f} grafite: {grafite_str} folhas: {self.folhas_escritas}"