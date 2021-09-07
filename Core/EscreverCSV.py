import csv
from csv import writer


class EscreverCSV:

    def escrevercsv(self, data):
        self.data = data
        data = self.data
        fim = 0

        with open('PYTHON\projetos\PFNoobs\Opening\Data\SAVE.csv', 'a+', newline='') as escreverFile:
            print("Salvando data: -> ", data)
            d2 = writer(escreverFile)
            d2.writerow(data)
        escreverFile.close()
        print("PROFILE CRIADO!")
        fim = 1
        return fim


ObjEscreverCSV = EscreverCSV()