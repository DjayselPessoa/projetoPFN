import csv
from csv import writer
from pathlib import Path
from pathlib import PureWindowsPath


class UpdateScore:

    def updatescore(self, score, cod, active, pegarDirRaiz):
        self.pegarDirRaiz = pegarDirRaiz
        self.score = score
        self.cod = cod
        self.active = active

        novoCod = str(cod)

        nomeArquivoSCORE = "score_"+novoCod+".csv"
        pathTratado = str(self.pegarDirRaiz)
        home = Path(pathTratado)
        sourcePath = Path(home, "Data", nomeArquivoSCORE)

        # print(self.score)
        data = [(self.score)]

        with open(sourcePath, "a+", newline='') as escreverFile:
            d2 = writer(escreverFile)
            d2.writerow(data)
            print("Salvando SCORE: -> ", data)
        escreverFile.close()
        print("SCORE ATUALIZADO!")
        return self.active


ObjUpdateScore = UpdateScore()
