class OpAssociacao:

    def opAssociacao(self, score):
        self.score = score
        escolhaMenu = ""
        resposta = ""
        print("-" * 99)
        active = True
        while active:
            print(f"score: {self.score}\nEscolha abaixo qual Operador de Associação você deseja aprender:\n","\n[1] - Dentro (in)\n[2] - Não em (not in)\n[3] - Voltar\n")
            escolhaMenu = str(input("Escolha uma opção: "))

            try:
                if escolhaMenu == "1":
                    print("\nO operador de Associação (in) verifica se o valor da esquerda está contido dentro da sequência dos valores da direita. Ex.:\n")
                    print("\nnumero1 = 2, numero2 = 3, lista = [1,3,4]")
                    print("[A] - if num1 in lista:")
                    print("[B] - if num2 in lista:")
                    resposta = str(input("\nInforme qual das duas opções acima A e B será executada: "))
                    if resposta in "Aa":
                        print("\nResposta errada! O valor da variável numero1 não está na sequência de valores da lista.")
                        self.score -= 1
                        raise ValueError("-" * 99)
                    elif resposta in "Bb":
                        print("\nResposta correta! O valor da variável numero2 está na sequência de valores da lista.")
                        self.score += 1
                        raise ValueError("-" * 99)
                    else:
                        print("\nCaractere inválido! REINICIANDO!")
                        raise ValueError("-" * 99)
                elif escolhaMenu == "2":
                    print("\nO operador de Associação (not in) verifica se o valor da esquerda não está contido dentro da sequência dos valores da direita:\n")
                    print("\nnumero1 = 2, numero2 = 3, lista = [1,3,4]")
                    print("[A] - if not num1 in lista:")
                    print("[B] - if not num2 in lista:")
                    resposta = str(input("\nInforme qual das duas opções acima A e B está correta: "))
                    if resposta in "Aa":
                        print("\nCorreto! O valor da variável num1 não está na sequência de valores da lista.")
                        self.score += 1
                        raise ValueError("-" * 99)
                    elif resposta in "Bb":
                        print("\nResposta incorreta! O valor da variável num2 está na sequência de valores da lista.")
                        self.score -= 1
                        raise ValueError("-" * 99)
                    else:
                        print("\nCaractere inválido! REINICIANDO!")
                        raise ValueError("-" * 99)
                elif escolhaMenu == "3":
                    print("\nSempre pergunte, não aceite a dúvida!\n")
                    return self.score
                else:
                    raise ValueError("\nDADO INCORRETO!")

            except ValueError as e:
                print(e)


ObjOpAssociacao = OpAssociacao()
