import csv
from pathlib import Path


class LerScore:

    def lerscore(self, nomeScore, pegarDirRaiz):
        try:
            self.pegarDirRaiz = pegarDirRaiz
            self.nomeScore = nomeScore
            # print(f"self.nomeScore: {self.nomeScore}")
            nomeArquivoSCORE = str(self.nomeScore)
            # print(f"nomeArquivoSCORE: {nomeArquivoSCORE}")
            home = Path(self.pegarDirRaiz)
            sourcePath = Path(home, "Data", nomeArquivoSCORE)
            # print(f"path completo: {sourcePath}")
            valorScoreUser = []
            nomeScoreUser = str
            ultimoScoreUser = 0

            objetoScore = csv.DictReader(open(sourcePath), delimiter='\n')  #  Obtendo dados
            for f in objetoScore:
                valorScoreUser.append(int(f["SCORE"]))
            ultimoScoreUser = int(valorScoreUser[-1])  # obtendo ultimo valor do score lido
            print(f'ultimo valor de score do usuário: {ultimoScoreUser}')
            return ultimoScoreUser
        except ValueError as e:
            print("LOG ->", e)


ObjLerScore = LerScore()
