import csv
from pathlib import Path


class LerScore:

    def lerscore(self, nomeScore, pegarDirRaiz):
        try:
            self.pegarDirRaiz = pegarDirRaiz
            self.nomeScore = nomeScore
            nomeArquivoSCORE = str(self.nomeScore)
            # print(f"nomeArquivoSCORE: {nomeArquivoSCORE}")
            home = Path(self.pegarDirRaiz)
            sourcePath = Path(home, "Data", nomeArquivoSCORE)
            # print(f"path completo: {sourcePath}")
            valorScoreUser = []
            #  Obtendo dados
            objetoScore = csv.DictReader(open(sourcePath), delimiter='\n')
            for f in objetoScore:
                valorScoreUser.append(int(f["SCORE"]))
            ultimoScoreUser = int(valorScoreUser[-1])  # obtendo ultimo valor do score lido
            # print(f'ultimo valor de score do usuário: {ultimoScoreUser} de nome: {self.nomeScore}')
            return ultimoScoreUser
        except ValueError as e:
            print("LOG: -> LerScoreErro", e)
            ultimoScoreUser = 0
            return ultimoScoreUser

ObjLerScore = LerScore()
