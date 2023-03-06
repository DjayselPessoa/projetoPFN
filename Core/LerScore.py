import csv
from pathlib import Path


class LerScore:

    def lerscore(self, nomeScore, pegarDirRaiz):
        self.pegarDirRaiz = pegarDirRaiz
        self.nomeScore = nomeScore

        scoreUser = []
        nomeArquivoSCORE = self. nomeScore
        home = Path(self.pegarDirRaiz)
        sourcePath = Path(home, "Data", nomeArquivoSCORE)

        for f in csv.DictReader(open(sourcePath), delimiter=','):
            scoreUser.append(f["SCORE"])

        # print(scoreUser)
        return scoreUser[len(scoreUser) - 1]


ObjLerScore = LerScore()