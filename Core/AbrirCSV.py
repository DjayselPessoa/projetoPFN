import csv


class AbrirCSV:

    def abrircsv(self):
        cod = []
        nome = []
        senha = []
        scorename = []

        for d in csv.DictReader(open('PYTHON\projetos\PFNoobs\Opening\Data\SAVE.csv'), delimiter=','):
            cod.append(d["COD"])
            nome.append(d["NOME"])
            senha.append(d["SENHA"])
            scorename.append(d["SCORENAME"])

        alertCod = len(cod)
        return alertCod, cod, nome, senha, scorename

    def abrirScore(self, alertscore):
        self.alertscore = alertscore
        scoreList = []
        novoCod = "#"+str(self.alertscore)
        novoCodNameFile = '_'+novoCod+'.csv'
        novoPath = 'PYTHON\projetos\PFNoobs\Opening\Data\score'+novoCodNameFile
        for d1 in csv.DictReader(open(novoPath), delimiter=','):
            scoreList.append(d1["SCORE"])

        return scoreList


ObjAbrirCSV = AbrirCSV()
ObjAbrirSCORE = AbrirCSV()
