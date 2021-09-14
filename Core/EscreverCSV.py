import csv
from csv import writer
from pathlib import Path
from time import sleep


class EscreverCSV:

    def escrevercsv(self, data, pegarDirRaiz):
        self.pegarDirRaiz = pegarDirRaiz
        self.data = data
        fim = 0
        pathTratado = str(self.pegarDirRaiz)
        home = Path(pathTratado)
        sourcePath = Path(home, "Data", "SAVE.csv")
        with open(sourcePath, 'a+', newline='') as escreverFile:
            sleep(1)
            print("Salvando DATA: -> {:^11s} -{:^13s}- {:^15s}".format("NOME", "ID", "SCOREFILE"))
            sleep(.5)
            print("Salvando DATA: -> {:^11s} -{:^13s}- {:^15s}".format(self.data[1], self.data[0], self.data[3]))
            d2 = writer(escreverFile)
            d2.writerow(data)
        escreverFile.close()
        sleep(1)
        print("PROFILE CRIADO!")
        fim = 1
        return fim


ObjEscreverCSV = EscreverCSV()
