from pathlib import Path
import csv


class AbrirCSV:

    def abrircsv(self, pegarDirRaiz):
        self.pegarDirRaiz = pegarDirRaiz
        cod = []
        nome = []
        senha = []
        scorename = []

        pathTratado = str(self.pegarDirRaiz)
        home = Path(pathTratado)
        sourcePath = Path(home, "Data", "SAVE.csv")
        sourcePath = str(sourcePath)
        # print("ok3", sourcePath)

        for d in csv.DictReader(open(sourcePath), delimiter=','):
            cod.append(d["COD"])
            nome.append(d["NOME"])
            senha.append(d["SENHA"])
            scorename.append(d["SCORENAME"])

        alertCod = len(cod)
        # print("quantidade cod abrirCSV -> ", len(cod))
        # print("type -> ", type(len(cod)))
        return alertCod, cod, nome, senha, scorename

    def abrirScore(self, pegarDirRaiz, position, cod):
        self.pegarDirRaiz = pegarDirRaiz
        self.position = position
        self.cod = cod
        scoreList = []
        novoCod = self.cod[self.position]
        nomeArquivoSCORE = "score_"+novoCod+".csv"

        pathTratado = str(self.pegarDirRaiz)
        home = Path(pathTratado)
        sourcePath = Path(home, "Data", nomeArquivoSCORE)
        # print(str(home))

        for d1 in csv.DictReader(open(sourcePath), delimiter=','):
            scoreList.append(d1["SCORE"])

        return scoreList


ObjAbrirCSV = AbrirCSV()
ObjAbrirSCORE = AbrirCSV()
