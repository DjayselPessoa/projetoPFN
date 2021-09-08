import csv
from csv import writer


class UpdateScore:

    def updatescore(self, score, cod, active):
        self.score = score
        self.cod = cod
        self.active = active

        nomePath = str(cod)
        createNamePath = "PYTHON\projetos\PFNoobs\Opening\Data\score_"+nomePath+".csv"
        # print(self.score)
        data = [(self.score)]

        with open(createNamePath, "a+", newline='') as escreverFile:
            d2 = writer(escreverFile)
            d2.writerow(data)
            print("Salvando SCORE: -> ", data)
        escreverFile.close()
        print("SCORE ATUALIZADO!")
        return self.active


ObjUpdateScore = UpdateScore()
