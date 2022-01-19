from PacoteDef.DefEscolha import ObjEscolha


class LayerMain:
    def layermain(self, nome, score, cod, active):
        self.cod = cod
        self.nome = nome
        self.score = score
        self.active = active

        sair = "no"
        escolhaOp = str

        while active:
            try:
                escolhaOp = str
                print("-" * 46)
                print("\n" + ("-" * 20) + "---- PYTHON FOR NOOBS ----")
                print("\n" + ("-" * 76) + "PFN-------DjPESSÔA -")             
                print(f"USER: {self.nome} <-> SCORE: {self.score}")
                print("\nAbaixo estão todos os tipos de operadores menos o bit a bit\nUtilize os números para escolher:\n\n[1] - Operadores Aritméticos\n[2] - Operadores de Atribuição\n[3] - Operadores de Comparação\n[4] - Operadores Lógicos\n[5] - Operadores de Identidade\n[6] - Operadores de Associação\n[7] - Sobre o programa\n[8] - Voltar\n","\n")
                escolhaOp = str(input("Qual operador deseja estudar: -> "))
                if escolhaOp not in "12345678":
                    raise ValueError("\nDADO INCORRETO - REINICIANDO!")
                else:
                    sair, self.score, codFinal = ObjEscolha.escolha(escolhaOp, self.score, self.cod)
                # print("scoreFinal", self.score)

                if sair == "ok":
                    self.active = False
                    # print("scoreInicio", self.score)
                    return self.active, self.score, codFinal
                elif sair == "no":
                    self.active = True
                else:
                    raise ValueError("\nERRO DESCONHECIDO!")

            except ValueError as e:
                print("\nLOG: -> ", e)


ObjLayerMain = LayerMain()
