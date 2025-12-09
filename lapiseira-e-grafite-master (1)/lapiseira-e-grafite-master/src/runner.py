from src.dureza import Dureza
from src.grafite import Grafite
from src.lapiseira import Lapiseira

if __name__ == '__main__':
    #Inserindo grafites
    lapiseira = Lapiseira(0.5)
    print(lapiseira)

    #Calibre imcompative
    if not lapiseira.inserir(Grafite(0.7, Dureza.G_2B,50)):
        print("fail: calibre incompatível")

    lapiseira.inserir(Grafite(0.5, Dureza.G_2B, 50))
    print(lapiseira)

    #Inserindo e Removendo
    lapiseira = Lapiseira(0.3)
    lapiseira.inserir(Grafite(0.3, Dureza.G_2B, 50))
    print(lapiseira)

    if not lapiseira.inserir(Grafite(0.3, Dureza.G_4B, 70)):
        print("fail: ja existe grafite")

    print(lapiseira)
    lapiseira.remover()
    lapiseira.inserir(Grafite(0.3, Dureza.G_4B, 70))

    #Escrevendo
    lapiseira = Lapiseira(0.9)
    lapiseira.inserir(Grafite(0.9, Dureza.G_4B,4))
    lapiseira.escrever(1)
    if not lapiseira.getGrafite():
        print("warning: grafite acabou")
    print(lapiseira)

    lapiseira.inserir(Grafite(0.9, Dureza.G_4B, 30))
    lapiseira.escrever(6)
    print(lapiseira)

    if not lapiseira.escrever(3):
        print("warning: grafite acabou")
        print(str(lapiseira.getFolhasEscritas()) + " folhas escritas com esse grafite no total")

    print(lapiseira)

    lapiseira = Lapiseira(0.9)
    lapiseira.inserir(Grafite(0.9, Dureza.G_2B, 15))
    print(lapiseira)

    lapiseira.escrever(4)
    print(lapiseira)

    if not lapiseira.escrever(4):
        print("warning: grafite acabou")
        print(str(lapiseira.getFolhasEscritas()) + " folhas escritas com esse grafite no total")

    print(lapiseira)