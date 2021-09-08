class OpComparacao:

    def opComparacao(self, score):
        self.score = score
        escolhaMenu = ""
        resposta = ""
        print("-" * 99)
        active = True
        while active:

            print(f"score: {self.score}\nEscolha abaixo qual Operador de Comparação você deseja aprender:\n","\n1 - Igual [==]\n2 - Diferente [!=]\n3 - Maior que [>]\n4 - Menor que [<]\n5 - Maior ou igual [>=]\n6 - Menor ou igual [<=]\n7 - Voltar\n")
            escolhaMenu = str(input("Escolha uma opção: "))

            try:
                if escolhaMenu == "1":
                    print("\nCom o operador Igual [==] podemos verificar se os valores de dois operandos são iguais. Se sim a condição se torna verdadeira.")
                    print("numero1 = 2 -> numero2 = 3")
                    print("If numero1 == numero2:")
                    print("\nCom esses valores das variáveis informe se o programa conseguirá acessar o bloco de código do If em questão")
                    resposta = input("S para sim, N para não: ")
                    resposta = str(resposta)
                    if resposta in 'Ss':
                        print("\nResposta incorreta! Os dois valores são diferentes!")
                        self.score -= 1
                        raise ValueError("-" * 99)
                    elif resposta in 'Nn':
                        print("\nResposta correta! Os valores são diferentes!")
                        self.score += 1
                        raise ValueError("-" * 99)
                    else:
                        print("\nCaractere inválido! REINICIANDO!")
                        raise ValueError("-" * 99)
                elif escolhaMenu == "2":
                    print("\nCom o operador Diferente [!=] podemos verificar se os valores de dois operandos são distintos. Se sim a condição se torna verdadeira.\n")
                    print("numero1 = 5 -> numero2 = 3")
                    print("If numero1 != numero2:")
                    print("\nCom esses valores das variáveis informe se o programa conseguirá acessar o bloco de código do If em questão")
                    resposta = input("S para sim, N para não: ")
                    resposta = str(resposta)
                    if resposta in 'Ss':
                        print("\nResposta correta! Os valores são diferentes!")
                        self.score += 1
                        raise ValueError("-" * 99)
                    elif resposta in 'Nn':
                        print("\nResposta incorreta! Os dois valores são diferentes!")
                        self.score -= 1
                        raise ValueError("-" * 99)
                    else:
                        print("\nCaractere inválido! REINICIANDO!")
                        raise ValueError("-" * 99)
                elif escolhaMenu == "3":
                    print("\nCom o operador Maior que [>] podemos verificar se o valor de um operando é maior que de outro operando. Se sim a condição se torna verdadeira.\n")
                    print("numero1 = 5 -> numero2 = 3")
                    print("If numero1 > numero2:")
                    print("\nCom esses valores das variáveis informe se o programa conseguirá acessar o bloco de código do If em questão")
                    resposta = input("S para sim, N para não: ")
                    resposta = str(resposta)
                    if resposta in 'Ss':
                        print("\nResposta correta! numero1 é maior que numero2")
                        self.score += 1
                        raise ValueError("-" * 99)
                    elif resposta in 'Nn':
                        print("\nResposta incorreta! numero1 é maior que numero2")
                        self.score -= 1
                        raise ValueError("-" * 99)
                    else:
                        print("\nCaractere inválido! REINICIANDO!")
                        raise ValueError("-" * 99)
                elif escolhaMenu == "4":
                    print("\nCom o operador Menor que [<] podemos verificar se o valor de um operando é menor que de outro operando. Se sim a condição se torna verdadeira.\n")
                    print("numero1 = 3 -> numero2 = 3")
                    print("If numero1 < numero2:")
                    print("\nCom esses valores das variáveis informe se o programa conseguirá acessar o bloco de código do If em questão")
                    resposta = input("S para sim, N para não: ")
                    resposta = str(resposta)
                    if resposta in 'Ss':
                        print("\nResposta incorreta! numero1 é igual numero2")
                        self.score -= 1
                        raise ValueError("-" * 99)
                    elif resposta in 'Nn':
                        print("\nResposta correta! numero1 não é menor que o numero2, eles são iguais.")
                        self.score += 1
                        raise ValueError("-" * 99)
                    else:
                        print("\nCaractere inválido! REINICIANDO!")
                        raise ValueError("-" * 99)
                elif escolhaMenu == "5":
                    print("\nCom o operador Maior ou igual [>=] podemos verificar se o valor de um operando é maior que de outro operando ou também se é igual. Se sim a condição se torna verdadeira.\n")
                    print("numero1 = 3 -> numero2 = 3")
                    print("If numero1 >= numero2:")
                    print("\nCom esses valores das variáveis informe se o programa conseguirá acessar o bloco de código do If em questão")
                    resposta = input("S para sim, N para não: ")
                    resposta = str(resposta)
                    if resposta in 'Ss':
                        print("\nResposta correta! numero1 não é maior mas é igual ao numero2")
                        self.score += 1
                        raise ValueError("-" * 99)
                    elif resposta in 'Nn':
                        print("\nResposta incorreta! numero1 é igual numero2, só não é maior.")
                        self.score -= 1
                        raise ValueError("-" * 99)
                    else:
                        print("\nCaractere inválido! REINICIANDO!")
                        raise ValueError("-" * 99)
                elif escolhaMenu == "6":
                    print("\nCom o operador Menor ou igual [<=] podemos verificar se o valor de um operando é menor que de outro operando ou se é igual. Se sim a condição se torna verdadeira.\n")
                    print("numero1 = 3 -> numero2 = 3")
                    print("If numero1 <= numero2:")
                    print("\nCom esses valores das variáveis informe se o programa conseguirá acessar o bloco de código do If em questão")
                    resposta = input("S para sim, N para não: ")
                    resposta = str(resposta)
                    if resposta in 'Ss':
                        print("\nResposta correta! numero1 não é menor mas é igual ao numero2")
                        self.score += 1
                        raise ValueError("-" * 99)
                    elif resposta in 'Nn':
                        print("\nResposta incorreta! numero1 é igual numero2, só não é menor.")
                        self.score -= 1
                        raise ValueError("-" * 99)
                    else:
                        print("\nCaractere inválido! REINICIANDO!")
                        raise ValueError("-" * 99)
                elif escolhaMenu == "7":
                    print("\nSempre procure soluções, se não encontrar procure mais!\n")
                    return self.score
                else:
                    raise ValueError("\nDADO INCORRETO!")

            except ValueError as e:
                print("\n", e)


ObjOpComparacao = OpComparacao()
