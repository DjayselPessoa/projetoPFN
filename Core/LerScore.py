import csv
from pathlib import Path


class LerScore:

    def lerscore(self, nomeScore, pegarDirRaiz):
        self.pegarDirRaiz = pegarDirRaiz
        self.nomeScore = nomeScore
        # print(f"self.nomeScore: {self.nomeScore}")
        scoreUser = []
        nomeArquivoSCORE = str(self.nomeScore)
        # print(f"nomeArquivoSCORE: {nomeArquivoSCORE}")
        home = Path(self.pegarDirRaiz)
        sourcePath = Path(home, "Data", nomeArquivoSCORE)
        # print(sourcePath)

        for f in csv.DictReader(open(sourcePath), delimiter=''):
            scoreUser.append(f["SCORE"])

        print(f'scoreUser: {scoreUser[int(len(scoreUser))]}')
        return scoreUser[len(scoreUser)]


ObjLerScore = LerScore()
