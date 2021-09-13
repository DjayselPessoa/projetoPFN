from Core.LerScore import ObjLerScore


class RankScore:

    def rankscore(self, cod, pegarDirRaiz, nome):
        try:
            self.cod = cod
            self.pegarDirRaiz = pegarDirRaiz
            self.nome = nome

            cont = 1
            maior = 0
            x = 0
            y = 0
            tickTack = 0
            local = []
            valorScore = []
            first = []
            active = True

            if len(self.cod) == 0:
                raise ValueError("SEM REGISTROS VÁLIDOS! REINICIANDO!")

            while active:

                for i in range(len(self.cod)):
                    if i == (len(self.cod) - 1):
                        active = False
                    if tickTack == 0:
                        nomeScore = "score_"+self.cod[cont - 1]+".csv"
                        scoreUser = ObjLerScore.lerscore(nomeScore, self.pegarDirRaiz)
                        x = int(scoreUser)
                        tickTack = 1
                        if maior < x:
                            maior = x
                            local.append(self.cod[cont - 1])
                            valorScore.append(x)
                            first.append(self.nome[cont - 1])
                            cont += 1
                            continue
                        cont += 1
                        continue
                    elif tickTack == 1:
                        nomeScore = "score_"+self.cod[cont - 1]+".csv"
                        scoreUser = ObjLerScore.lerscore(nomeScore, self.pegarDirRaiz)
                        y = int(scoreUser)
                        tickTack = 0

                        if maior < y:
                            maior = y
                            local.append(self.cod[cont - 1])
                            valorScore.append(y)
                            first.append(self.nome[cont - 1])
                            cont += 1
                            continue
                        cont += 1
                        continue
            else:

                victory = len(local) - 1

                print("{:^11s}{:^13s}{:^11s}".format("NOME", "ID PESSOAL", "SCORE"))
                print("{:^11s}{:^13s}{:^11s}".format(str(first[victory]), str(local[victory]), str(valorScore[victory])))
                raise ValueError("SCORE TERMINADO!")

        except ValueError as e:
            print("\nLOG: -> ", e)


ObjRankScore = RankScore()
