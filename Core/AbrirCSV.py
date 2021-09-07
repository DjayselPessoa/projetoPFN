import csv


class AbrirCSV:

    def abrircsv(self):
        cod = []
        nome = []
        senha = []
        score = []

        for d in csv.DictReader(open('PYTHON\projetos\PFNoobs\Opening\Data\SAVE.csv'), delimiter=','):
            cod.append(d["COD"])
            nome.append(d["NOME"])
            senha.append(d["SENHA"])
            score.append(d["SCORE"])

        alert = len(cod)
        return alert, cod, nome, senha, score


ObjAbrirCSV = AbrirCSV()