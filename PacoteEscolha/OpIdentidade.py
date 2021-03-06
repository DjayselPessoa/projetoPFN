class OpIdentidade:

    def opIdentidade(self, score):
        self.score = score
        escolhaMenu = ""
        num1 = 2
        num2 = 3
        print("-" * 99)
        active = True
        while active:

            print(f"score: {self.score}\nEscolha abaixo qual Operador de identidade você deseja aprender:\n","\n[1] - É (is)\n[2] - Não é (is not)\n[3] - Voltar\n")
            escolhaMenu = str(input("Escolha uma opção: "))

            try:
                if escolhaMenu == "1":
                    print("\nO operador de Identidade (is) a primeira vista pode parecer funcionar igual ao operador de comparação (==).\nEntretanto, enquanto (==) compara valores o operador de identidade compara se apontam para o mesmo objeto na memória.")
                    print("Em suma, o operador de identidade (is) não deve ser usado para substituir o operador de comparação (==) em nenhuma circunstância. Ex.:\n")
                    print("numero1 = 2", id(num1), "\nnumero2 = 3", id(num2))
                    print("Acima você está vendo que numero1 contém o valor 2, entretanto o seu identificador na memória é outro valor. O mesmo para o número 2.")
                    self.score += 1
                    raise ValueError("-" * 99)
                elif escolhaMenu == "2":
                    print("\nO operador de Identidade (is not) também pode parecer funcionar igual ao operador de comparação (!=).\nEntretanto (!=) verifica se os valores são diferentes enquanto o operador de identidade compara se esses valores não apontam para o mesmo objeto na memória.")
                    print("Em suma, o operador de identidade (is not) não deve ser usado para substituir o operador de comparação (!=) em nenhuma circunstância. Ex.:\n")
                    print("numero1 = 2", id(num1), "\nnumero2 = 3", id(num2))
                    print("Acima você está vendo que numero1 contém o valor 2, entretanto o seu identificador na memória é outro valor. O mesmo para o número 2.")
                    self.score += 1
                    raise ValueError("-" * 99)
                elif escolhaMenu == "3":
                    print("\nSempre pergunte, não aceite a dúvida!\n")
                    return self.score
                else:
                    raise ValueError("\nDADO INCORRETO!")

            except ValueError as e:
                print(e)


ObjOpIdentidade = OpIdentidade()
