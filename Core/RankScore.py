from Core.LerScore import ObjLerScore
from time import sleep


class RankScore:

    def rankscore(self, pegarDirRaiz, cod, nome, active):

        self.pegarDirRaiz = pegarDirRaiz  # string
        self.active = active  # boolean
        self.cod = cod  # lista
        self.nome = nome  # lista

        cont = 0  # contador
        # -------------------------------------------------------------------------------------------------
        # variáveis de comparação:
        # -------------------------------------------------------------------------------------------------
        #
        # -------------------------------------------------------------------------------------------------

        linha = "-" * 40
        scoreUser = 0
        scoreAll = {}
        nomeAll = {}
        # print("rank var")

        while self.active:
            try:
                # print(len(self.cod))
                print(f"len lista cod: {len(self.cod)}")
                if len(self.cod) == 1:
                    nomeScore = "score_"+str(self.cod[0])+".csv"
                    print(f"nomeScore completo: {nomeScore}")
                    scoreUser = ObjLerScore.lerscore(nomeScore, self.pegarDirRaiz)
                    print(f"scoreUser retornado: {scoreUser}")
                    if scoreUser == 0:
                        self.active = False
                        raise ValueError("Score Zero não são mostrados!\nREINICIANDO")
                    else:
                        print(linha)
                        print("|{:^11s}|{:^13s}|{:^11s}|".format("NOME", "ID PESSOAL", "SCORE"))
                        print(linha)
                        sleep(.5)
                        print("|{:^11s}|{:^13s}|{:^11s}|".format(str(self.nome[0]), str(self.cod[0]), str("1º")))
                        print(linha)
                        ValueError("LOADING -> ")

                elif len(self.cod) > 1:
                    notFull = True
                    while notFull:
                        for i in self.cod:
                            print(f"elemento de cod: {i}")
                            nomeScore = "score_"+str(self.cod[cont])+".csv"
                            print(f"nomeScore completo: {nomeScore}")
                            scoreUser = ObjLerScore.lerscore(nomeScore, self.pegarDirRaiz)
                            print(f"scoreUser retornado: {scoreUser}")
                            scoreAll[str(self.cod[cont])] = scoreUser
                            nomeAll[str(self.cod[cont])] = self.nome[cont]
                            cont += 1
                        for x in scoreAll:
                            print(x)

            except ValueError as e:
                sleep(1)
                print("\nLOG: -> ", str(e))


ObjRankScore = RankScore()
