import csv
from pathlib import Path


class LerScore:

    def lerscore(self, nomeScore, pegarDirRaiz):
        try:
            self.pegarDirRaiz = pegarDirRaiz
            self.nomeScore = nomeScore
            # print(f"self.nomeScore: {self.nomeScore}")
            scoreUser = []
            nomeArquivoSCORE = str(self.nomeScore)
            # print(f"nomeArquivoSCORE: {nomeArquivoSCORE}")
            home = Path(self.pegarDirRaiz)
            sourcePath = Path(home, "Data", nomeArquivoSCORE)
            # print(sourcePath)
            cont2 = 0
            objetoScore = csv.DictReader(open(sourcePath), delimiter=',')
            for f in objetoScore:
                scoreUser.append(f["SCORE"])
                print(f"cont2: {cont2} - lista {scoreUser[cont2]}")
                cont2 += 1
            mostrar = scoreUser[cont2]
            print(f'scoreUser: {mostrar}')
            return mostrar
        except ValueError as e:
            print("LOG ->", e)


ObjLerScore = LerScore()
