class OpAtribuicao:

    def opAtribuicao(self, score):
        self.score = score
        escolhaMenu = ""
        num1 = 0
        num2 = 0
        print("-" * 99)
        active = True
        while active:

            print(f"score: {self.score}\nOperadores de Atrubuição:\n","\n[1] - Atribuição simples (=)\n[2] - Incremento (+=)\n[3] - Decremento (-=)\n[4] - Dividido igual (/=)\n[5] - Vezes igual (*=)\n[6] - Módulo igual (%=)\n[7] - Voltar\n")
            escolhaMenu = str(input("Escolha uma opção: "))

            try:
                if escolhaMenu == "1":
                    print("\nO operador de atribuição simples faz com que os valores do lado direito do operador sejam atribuido ao que estiver do lado esquerdo, normalmente uma variável.")
                    num1 = int(input("Informe um número inteiro: "))
                    num2 = int(input("Informe outro número inteiro: "))
                    print(f"\nvariavelExemplo = {num1} + {num2}; variavelExemplo possui ou representa o valor {num1 + num2}\n")
                    self.score += 1
                    raise ValueError("-" * 99)
                elif escolhaMenu == "2":
                    print("\nO operador de incremento faz com que os valores da variável do lado esquerdo seja somada ao valores do lado direito e por fim reatribuído à variável.\n")
                    num1 = int(input("Informe um número inteiro que será o valor da variávelExemplo: "))
                    num2 = int(input("Informe outro número inteiro: "))
                    print(f"\nvariavelExemplo += {num2}, isso é o mesmo que escrever: variavelExemplo = variavelExemplo + {num2}. A variavelExemplo ao final possuirá o valor {num1 + num2}")
                    self.score += 1
                    raise ValueError("-" * 99)
                elif escolhaMenu == "3":
                    print("\nO operador de decremento faz com que os valores da variável do lado esquerdo seja subtraída pelo valor do lado direito e por fim reatribuído à variável.\n")
                    num1 = int(input("Informe um número inteiro que será o valor da variávelExemplo: "))
                    num2 = int(input("Informe outro número inteiro: "))
                    print(f"\nvariavelExemplo -= {num2}, isso é o mesmo que escrever: variavelExemplo = variavelExemplo - {num2}. A variavelExemplo ao final possuirá o valor {num1 - num2}")
                    self.score += 1
                    raise ValueError("-" * 99)
                elif escolhaMenu == "4":
                    print("\nO operador dividido igual faz com que os valores da variável do lado esquerdo seja dividido pelo valor do lado direito e por fim reatribuído à variável\n")
                    num1 = int(input("Informe um número inteiro que será o valor da variávelExemplo: "))
                    num2 = int(input("Informe outro número inteiro: "))
                    print(f"\nvariavelExemplo /= {num2}, isso é o mesmo que escrever: variavelExemplo = variavelExemplo / {num2}. A variavelExemplo ao final possuirá o valor {num1 / num2}")
                    self.score += 1
                    raise ValueError("-" * 99)
                elif escolhaMenu == "5":
                    print("\nO operador vezes igual faz com que os valores da variável do lado esquerdo seja multiplicado pelo valor do lado direito e por fim reatribuído à variável\n")
                    num1 = int(input("Informe um número inteiro que será o valor da variávelExemplo: "))
                    num2 = int(input("Informe outro número inteiro: "))
                    print(f"\nvariavelExemplo *= {num2}, isso é o mesmo que escrever: variavelExemplo = variavelExemplo * {num2}. A variavelExemplo ao final possuirá o valor {num1 * num2}")
                    self.score += 1
                    raise ValueError("-" * 99)
                elif escolhaMenu == "6":
                    print("\nO operador módulo igual faz com que os valores da variável do lado esquerdo receba o resto da divisão pelo valor do lado direito e por fim reatribuído à variável\n")
                    num1 = int(input("Informe um número inteiro que será o valor da variávelExemplo: "))
                    num2 = int(input("Informe outro número inteiro: "))
                    print(f"\nvariavelExemplo %= {num2}, isso é o mesmo que escrever: variavelExemplo = variavelExemplo % {num2}. A variavelExemplo ao final possuirá o valor {num1 % num2}")
                    self.score += 1
                    raise ValueError("-" * 99)
                elif escolhaMenu == "7":
                    print("\nMelhor forma de aprender é testando!\n")
                    return self.score
                else:
                    raise ValueError("\nDADO INCORRETO!")

            except ValueError as e:
                print(e)


ObjOpAtribuicao = OpAtribuicao()
