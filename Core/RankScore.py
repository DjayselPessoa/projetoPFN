from Core.LerScore import ObjLerScore
from time import sleep


class RankScore:

    def rankscore(self, pegarDirRaiz, cod, nome, active):
        try:
            self.cod = cod
            self.pegarDirRaiz = pegarDirRaiz
            self.nome = nome
            self.active = active

            cont = 1
            maior1 = 0
            maior2 = 0
            maior3 = 0
            x = 0
            y = 0
            tickTack = 0
            local1 = []
            local2 = []
            local3 = []
            valorScore1 = []
            valorScore2 = []
            valorScore3 = []
            first = []
            second = []
            third = []
            evitar1 = str
            evitar2 = str

            if len(self.cod) == 0:
                sleep(1)
                raise ValueError("SEM REGISTROS VÁLIDOS! REINICIANDO!")

            while self.active:
                # print(f"código tmh: {len(self.cod)}")
                for i in range(len(self.cod)):
                    # print(f"cont 0: {cont}")
                    # print(f"i: {i}")
                    if i == (len(self.cod) - 1):
                        self.active = False
                    if tickTack == 0:
                        nomeScore = "score_"+self.cod[cont - 1]+".csv"
                        # print("score name: "+nomeScore)
                        scoreUser = ObjLerScore.lerscore(nomeScore, self.pegarDirRaiz)
                        x = int(scoreUser)
                        tickTack = 1
                        if maior1 < x:
                            maior1 = x
                            local1.append(self.cod[cont - 1])
                            valorScore1.append(x)
                            first.append(self.nome[cont - 1])
                            cont += 1
                            # print(f"cont 1a: {cont}")
                            continue
                        cont += 1
                        # print(f"cont 1: {cont}")
                        continue
                    elif tickTack == 1:
                        # print("ok2")
                        nomeScore = "score_"+self.cod[cont - 1]+".csv"
                        # print("score name: "+nomeScore)
                        scoreUser = ObjLerScore.lerscore(nomeScore, self.pegarDirRaiz)
                        y = int(scoreUser)
                        tickTack = 0

                        if maior1 < y:
                            maior1 = y
                            local1.append(self.cod[cont - 1])
                            valorScore1.append(y)
                            first.append(self.nome[cont - 1])
                            cont += 1
                            # print(f"cont 2a: {cont}")
                            continue
                        cont += 1
                        # print(f"cont 2: {cont}")
                        continue
                victory1 = len(local1)
                # print(f"tamaho lista v: {victory1} - cont: {cont}")
                if len(self.cod) - 2 >= 0 and self.active is False:
                    cont = 1
                    tickTack = 0
                    self.active = True
                    evitar1 = "score_"+local1[len(local1) - 1]+".csv"
                    for i in range(len(self.cod)):
                        if i == (len(self.cod) - 1):
                            self.active = False
                        if tickTack == 0:
                            nomeScore = "score_"+self.cod[cont - 1]+".csv"
                            if nomeScore == evitar1:
                                tickTack = 1
                                cont += 1
                                continue
                            scoreUser = ObjLerScore.lerscore(nomeScore, self.pegarDirRaiz)
                            x = int(scoreUser)
                            tickTack = 1
                            if maior2 < x:
                                maior2 = x
                                local2.append(self.cod[cont - 1])
                                valorScore2.append(x)
                                second.append(self.nome[cont - 1])
                                cont += 1
                                continue
                            cont += 1
                            continue
                        elif tickTack == 1:
                            nomeScore = "score_"+self.cod[cont - 1]+".csv"
                            if nomeScore == evitar1:
                                tickTack = 0
                                cont += 1
                                continue
                            scoreUser = ObjLerScore.lerscore(nomeScore, self.pegarDirRaiz)
                            y = int(scoreUser)
                            tickTack = 0

                            if maior2 < y:
                                maior2 = y
                                local2.append(self.cod[cont - 1])
                                valorScore2.append(y)
                                second.append(self.nome[cont - 1])
                                cont += 1
                                continue
                            cont += 1
                            continue
                victory2 = len(local2)
                if len(self.cod) - 3 >= 0 and self.active is False:
                    cont = 1
                    tickTack = 0
                    self.active = True
                    evitar1 = "score_"+local1[len(local1) - 1]+".csv"
                    evitar2 = "score_"+local2[len(local2) - 1]+".csv"
                    # print(local2)
                    for i in range(len(self.cod)):
                        if i == (len(self.cod) - 1):
                            self.active = False
                        if tickTack == 0:
                            nomeScore = "score_"+self.cod[cont - 1]+".csv"
                            if nomeScore == evitar1 or nomeScore == evitar2:
                                tickTack = 1
                                cont += 1
                                continue
                            scoreUser = ObjLerScore.lerscore(nomeScore, self.pegarDirRaiz)
                            x = int(scoreUser)
                            # print(x)
                            tickTack = 1
                            if maior3 < x:
                                maior3 = x
                                # print(maior3)
                                local3.append(self.cod[cont - 1])
                                valorScore3.append(x)
                                third.append(self.nome[cont - 1])
                                cont += 1
                                continue
                            cont += 1
                            continue
                        elif tickTack == 1:
                            nomeScore = "score_"+self.cod[cont - 1]+".csv"
                            if nomeScore == evitar1 or nomeScore == evitar2:
                                tickTack = 0
                                cont += 1
                                continue
                            scoreUser = ObjLerScore.lerscore(nomeScore, self.pegarDirRaiz)
                            y = int(scoreUser)
                            tickTack = 0

                            if maior3 < y:
                                maior3 = y
                                local3.append(self.cod[cont - 1])
                                valorScore3.append(y)
                                third.append(self.nome[cont - 1])
                                cont += 1
                                continue
                            cont += 1
                            continue
                victory3 = len(local3)
                # print(victory3)
                # print(local3)
            else:
                if victory1 > 0:
                    if victory2 > 0:
                        if victory3 > 0:
                            linha = "-" * 40
                            print(linha)
                            print("|{:^11s}|{:^13s}|{:^11s}|".format("NOME", "ID PESSOAL", "SCORE"))
                            print(linha)
                            sleep(.5)
                            print("|{:^11s}|{:^13s}|{:^11s}|".format(str(first[victory1 - 1]), str(local1[victory1 - 1]), str(valorScore1[victory1 - 1])))
                            print(linha)
                            sleep(.5)
                            print("|{:^11s}|{:^13s}|{:^11s}|".format(str(second[victory2 - 1]), str(local2[victory2 - 1]), str(valorScore2[victory2 - 1])))
                            print(linha)
                            sleep(.5)
                            print("|{:^11s}|{:^13s}|{:^11s}|".format(str(third[victory3 - 1]), str(local3[victory3 - 1]), str(valorScore3[victory3 - 1])))
                            print(linha)
                            sleep(.5)
                            raise ValueError("SCORE TERMINADO - LOADING!\n"+linha)
                        else:
                            linha = "-" * 40
                            print(linha)
                            print("|{:^11s}|{:^13s}|{:^11s}|".format("NOME", "ID PESSOAL", "SCORE"))
                            print(linha)
                            sleep(.5)
                            print("|{:^11s}|{:^13s}|{:^11s}|".format(str(first[victory1 - 1]), str(local1[victory1 - 1]), str(valorScore1[victory1 - 1])))
                            print(linha)
                            sleep(.5)
                            print("|{:^11s}|{:^13s}|{:^11s}|".format(str(second[victory2 - 1]), str(local2[victory2 - 1]), str(valorScore2[victory2 - 1])))
                            print(linha)
                            sleep(.5)
                            raise ValueError("SCORE TERMINADO - LOADING!\n"+linha)
                    else:
                        linha = "-" * 40
                        print(linha)
                        print("|{:^11s}|{:^13s}|{:^11s}|".format("NOME", "ID PESSOAL", "SCORE"))
                        print(linha)
                        sleep(.5)
                        print("|{:^11s}|{:^13s}|{:^11s}|".format(str(first[victory1 - 1]), str(local1[victory1 - 1]), str(valorScore1[victory1 - 1])))
                        print(linha)
                        sleep(.5)
                        raise ValueError("SCORE TERMINADO - LOADING!\n"+linha)
                else:
                    linha = "-" * 40
                    print(linha)
                    print("|{:^11s}|{:^13s}|{:^11s}|".format("", "SCORE ZERO", ""))
                    print(linha)
        except ValueError as e:
            sleep(1)
            print("LOG: -> ", e)


ObjRankScore = RankScore()
