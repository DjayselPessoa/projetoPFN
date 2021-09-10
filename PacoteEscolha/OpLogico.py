class OpLogico:

    def oplogico(self, score):
        self.score = score
        escolhaMenu = ""
        resposta = ""
        print("-" * 99)
        active = True
        while active:

            print(f"score: {self.score}\nEscolha abaixo qual Operador lógico você deseja aprender:\n","\n1 - E lógico [and]\n2 - Ou lógico [or]\n3 - Não lógico [not]\n4 - Voltar\n")
            escolhaMenu = str(input("Escolha uma opção: "))

            try:
                if escolhaMenu == "1":
                    print("\nO operador E lógico [and] retorna Verdadeiro apenas se ambos os testes lógicos forem Verdadeiros, caso contrário, ele retorna Falso.")
                    print("Os testes lógicos normalmente são condições de teste para poder acessar algum bloco de código. Esses tipo de operador permite que mais de uma condição seja testada num mesmo IF. Ex.:\n")
                    print("numero1 = 2 -> numero2 = 3 -> numero3 = 4")
                    print("If numero1 > numero2 and numero3 > numero2:")
                    print("\nCom esses valores das variáveis informe se o programa conseguirá acessar o bloco de código do If em questão")
                    resposta = input("S para sim, N para não: ")
                    resposta = str(resposta)
                    if resposta in 'Ss':
                        print("\nResposta incorreta! O E lógico só é verdadeiro quando todas as condições são verdadeiras!")
                        self.score -= 1
                        raise ValueError("-" * 99)
                    elif resposta == 'N' or resposta == 'n':
                        print("\nResposta correta! ")
                        self.score += 1
                        raise ValueError("-" * 99)
                    else:
                        print("\nCaractere inválido! REINICIANDO!")
                        raise ValueError("-" * 99)
                elif escolhaMenu == "2":
                    print("\nO operador Ou lógico [or] retorna Verdadeiro quando pelo menos um dos testes lógicos for Verdadeiro, caso contrário, ele retorna Falso.")
                    print("Os testes lógicos normalmente são condições de teste para poder acessar algum bloco de código. Esses tipo de operador permite que mais de uma condição seja testada num mesmo IF. Ex.:\n")
                    print("numero1 = 2 -> numero2 = 3 -> numero3 = 4")
                    print("If numero1 > numero2 or numero3 > numero2:")
                    print("\nCom esses valores das variáveis informe se o programa conseguirá acessar o bloco de código do If em questão")
                    resposta = str(input("S para sim, N para não: "))
                    if resposta in "Ss":
                        print("\nResposta correta! ")
                        self.score += 1
                        raise ValueError("-" * 99)
                    elif resposta in "Nn":
                        print("\nResposta incorreta! O Ou lógico é verdadeiro quando ao menos uma condição for verdadeira!")
                        self.score -= 1
                        raise ValueError("-" * 99)
                    else:
                        print("\nCaractere inválido! REINICIANDO!")
                        raise ValueError("-" * 99)
                elif escolhaMenu == "3":
                    print("\nO operador Não lógico [not] inverte a condição.")
                    print("Os testes lógicos normalmente são condições de teste para poder acessar algum bloco de código. Ex.:\n")
                    print("numero1 = 2 -> numero2 = 3 -> numero3 = 4")
                    print("If not numero1 > numero2:")
                    print("\nCom essa condição o bloco de código do if em questão será executado ou não:")
                    resposta = str(input("S para sim, N para não: "))
                    if resposta in "Ss":
                        print("\nResposta correta! O número 1 não é maior que o numero 2.")
                        self.score += 1
                        raise ValueError("-" * 99)
                    elif resposta in "Nn":
                        print("\nResposta incorreta! O bloco do if será executado já que o número 1 de fato não é maior que o número 2!")
                        self.score -= 1
                        raise ValueError("-" * 99)
                    else:
                        print("\nCaractere inválido! REINICIANDO!")
                        raise ValueError("-" * 99)
                elif escolhaMenu == "4":
                    print("\nLeia e codifique!\n")
                    return self.score
                else:
                    raise ValueError("\nDADO INCORRETO!")

            except ValueError as e:
                print(e)


ObjOpLogico = OpLogico()
