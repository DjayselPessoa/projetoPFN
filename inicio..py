from PacoteDef.DefEscolha import ObjEscolha


class Inicio:
    def inicio(self, nome, score, active):
        self.nome = nome
        nome = self.nome
        self.score = score
        score = self.score
        self.active = active
        active = self.active

        sair = ""
        print("\n---- PYTHON FOR NOOBS ----\n")

        while active:
            try:
                escolhaOp = ""
                print("\n", "-" * 76, "PFN-------DjPESSÔA -")
                print(f"User: {nome} <-> SCORE: {score}")
                print("\nAbaixo estão todos os tipos de operadores:\n","\n1 - Operadores Aritméticos\n2 - Operadores de Atribuição\n3 - Operadores de Comparação\n4 - Operadores Lógicos\n5 - Operadores de Identidade\n6 - Operadores de Associação\n7 - Sobre o programa\n8 - Sair\n","\n")
                escolhaOp = str(input("Escolha qual destes tipos de operadores você deseja estudar: "))
                sair = ObjEscolha.escolha(escolhaOp)
                if sair == "ok":
                    active = False
                    return active

            except ValueError as e:
                print("Erro", e)


ObjInicio = Inicio()
