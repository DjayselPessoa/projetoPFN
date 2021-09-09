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

                print(" " * 15,"---- PYTHON FOR NOOBS ----\n")
                print("\n", "-" * 76, "PFN-------DjPESSÔA -")             
                print(f"User: {self.nome} <-> SCORE: {self.score}")
                print("\nAbaixo estão todos os tipos de operadores:\n\n1 - Operadores Aritméticos\n2 - Operadores de Atribuição\n3 - Operadores de Comparação\n4 - Operadores Lógicos\n5 - Operadores de Identidade\n6 - Operadores de Associação\n7 - Sobre o programa\n8 - Sair\n","\n")
                escolhaOp = str(input("Escolha os operadores que deseja estudar: "))
                sair, self.score, codFinal = ObjEscolha.escolha(escolhaOp, self.score, self.cod)
                # print("scoreFinal", self.score)

                if sair == "ok":
                    self.active = False
                    # print("scoreInicio", self.score)
                    return self.active, self.score, codFinal
                elif sair == "no":
                    self.active = True
                else:
                    raise ValueError("ERRO DESCONHECIDO!")

            except ValueError as e:
                print("LOG: -> ", e)


ObjLayerMain = LayerMain()
