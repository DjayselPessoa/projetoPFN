from Core.LerScore import ObjLerScore
from time import sleep


class RankScore:

    def rankscore(self, pegarDirRaiz, cod, nome, active):
        try:

            self.pegarDirRaiz = pegarDirRaiz  # string
            self.active = active  # boolean
            self.cod = cod  # lista
            self.nome = nome  # lista

            cont = 0  # contador
            nomeCod = {}  # dicionário dos 3 primeiros colocados
            scoreCod = {}  # dicionário dos 3 valores
            # -------------------------------------------------------------------------------------------------
            # variáveis de comparação:
            # -------------------------------------------------------------------------------------------------
            x = 0
            y = 0
            z = 0
            # -------------------------------------------------------------------------------------------------
            # controle por pulso:
            # -------------------------------------------------------------------------------------------------
            tickTack = 0
            # -------------------------------------------------------------------------------------------------
            scoreUser = [] 
            quant = len(self.cod)
            # print("rank var")
            if quant == 0:
                sleep(1)
                raise ValueError("SEM REGISTROS VÁLIDOS! REINICIANDO!")

            while self.active:
                # print("while")
                # print(len(self.cod))
                print(f"len cod: {len(self.cod)}")
                for i in range(0, len(self.cod)):
                    print(f"i: {i}")
                    # print(f"tt: {tickTack}")
                    # if i == (len(self.cod)-1):
                    #         active = False
                    # print(f"tt {tickTack}")
                    if tickTack == 0:
                        print(f"self.cod: {self.cod}")
                        nomeScore = "score_"+str(self.cod[i])+".csv"
                        print(f"nomeS: {nomeScore}")
                        scoreUser = ObjLerScore.lerscore(nomeScore, self.pegarDirRaiz)
                        print(f"scoreUser: {scoreUser}")
                        for w in scoreUser:
                            print(f"sUser: {w}")
                            cont += 1
                        x = int(scoreUser)
                        tickTack = 1
                        if maior1 < x:
                            maior1 = x
                            local1.append(self.cod[cont - 1])
                            valorScore1.append(x)
                            first.append(self.nome[cont - 1])
                            cont += 1
                            continue
                        cont += 1
                        continue
                    elif tickTack == 1:
                        nomeScore = "score_"+self.cod[i]+".csv"
                        scoreUser = ObjLerScore.lerscore(nomeScore, self.pegarDirRaiz)
                        y = int(scoreUser)
                        print(f"y: {y}")
                        tickTack = 0

                        if maior1 < y:
                            maior1 = y
                            local1.append(self.cod[cont - 1])
                            valorScore1.append(y)
                            first.append(self.nome[cont - 1])
                            cont += 1
                            continue
                        cont += 1
                        continue
                victory1 = len(local1)
                if len(cod) - 2 > 0 and active == False:
                    cont = 1
                    tickTack = 0
                    active = True
                    evitar1 = "score_"+local1[len(local1) - 1]+".csv"
                    for i in range(len(self.cod)):
                        if i == (len(self.cod) - 1):
                            active = False
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
                if len(cod) - 3 > 0 and active == False:
                    cont = 1
                    tickTack = 0
                    active = True
                    evitar1 = "score_"+local1[len(local1) - 1]+".csv"
                    evitar2 = "score_"+local2[len(local2) - 1]+".csv"
                    # print(local2)
                    for i in range(len(self.cod)):
                        if i == (len(self.cod) - 1):
                            active = False
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
                    print("ok1")
                    if victory2 > 0:
                        print("ok2")
                        if victory3 > 0:
                            print("ok3")
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
                    print(linha)
                    sleep(.5)
                    raise ValueError("Não há score para mostrar!\n"+linha)
        except ValueError as e:
            sleep(1)
            print("LOG: -> ", e)


ObjRankScore = RankScore()
