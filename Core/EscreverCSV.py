import csv
from csv import writer
from pathlib import Path
from pathlib import PureWindowsPath


class EscreverCSV:

    def escrevercsv(self, data, pegarDirRaiz):
        self.pegarDirRaiz = pegarDirRaiz
        self.data = data
        fim = 0
        pathTratado = str(self.pegarDirRaiz)
        home = Path(pathTratado)
        sourcePath = Path(home, "Data", "SAVE.csv")
        with open(sourcePath, 'a+', newline='') as escreverFile:
            print("Salvando data: -> ", self.data)
            d2 = writer(escreverFile)
            d2.writerow(data)
        escreverFile.close()
        print("PROFILE CRIADO!")
        fim = 1
        return fim


ObjEscreverCSV = EscreverCSV()
