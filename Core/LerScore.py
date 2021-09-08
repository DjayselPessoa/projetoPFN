import csv


class LerScore:

    def lerscore(self, position):
        self.position = position
        position = self.position

        scoreUser = []
        codPath = "#"+str(position - 1)
        createNamePath = "PYTHON\projetos\PFNoobs\Opening\Data\score_"+codPath+".csv"

        for f in csv.DictReader(open(createNamePath), delimiter=','):
            scoreUser.append(f["SCORE"])

        print(scoreUser)
        return scoreUser


ObjLerScore = LerScore()
