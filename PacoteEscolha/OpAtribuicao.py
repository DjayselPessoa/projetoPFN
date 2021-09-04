class OpAtribuicao:

    def opAtribuicao(self):
        escolhaMenu = ""
        num1 = 0
        num2 = 0
        print("---------------------------------------------------------------------------------------------------")

        print("\nOperadores de Atrubuição:\n","\n1 - Atribuição simples [=]\n2 - Incremento [+=]\n3 - Decremento [-=]\n4 - Dividido igual [/=]\n5 - Vezes igual [*=]\n6 - Módulo igual [%=]\n7 - Voltar\n")
        escolhaMenu = str(input("Escolha uma opção: "))

        try:
            if escolhaMenu == "1":
                print("O operador de atribuição simples faz com que os valores do lado direito do operador sejam atribuido ao que estiver do lado esquerdo, normalmente uma variável.")
                num1 = int(input("Informe um número inteiro: "))
                num2 = int(input("Informe outro número inteiro: "))
                print(f"variavelExemplo = {num1} + {num2}; variavelExemplo possui ou representa o valor {num1 + num2}\n")
                ObjOpAtribuicao.opAtribuicao()
            elif escolhaMenu == "2":
                print("O operador de incremento faz com que os valores da variável do lado esquerdo seja somada ao valores do lado direito e por fim reatribuído à variável.\n")
                num1 = int(input("Informe um número inteiro que será o valor da variávelExemplo: "))
                num2 = int(input("Informe outro número inteiro: "))
                print(f"variavelExemplo += {num2}, isso é o mesmo que escrever: variavelExemplo = variavelExemplo + {num2}. A variavelExemplo ao final possuirá o valor {num1 + num2}")
                ObjOpAtribuicao.opAtribuicao()
            elif escolhaMenu == "3":
                print("O operador de decremento faz com que os valores da variável do lado esquerdo seja subtraída pelo valor do lado direito e por fim reatribuído à variável.\n")
                num1 = int(input("Informe um número inteiro que será o valor da variávelExemplo: "))
                num2 = int(input("Informe outro número inteiro: "))
                print(f"variavelExemplo -= {num2}, isso é o mesmo que escrever: variavelExemplo = variavelExemplo - {num2}. A variavelExemplo ao final possuirá o valor {num1 - num2}")
                ObjOpAtribuicao.opAtribuicao()
            elif escolhaMenu == "4":
                print("O operador dividido igual faz com que os valores da variável do lado esquerdo seja dividido pelo valor do lado direito e por fim reatribuído à variável\n")
                num1 = int(input("Informe um número inteiro que será o valor da variávelExemplo: "))
                num2 = int(input("Informe outro número inteiro: "))
                print(f"variavelExemplo /= {num2}, isso é o mesmo que escrever: variavelExemplo = variavelExemplo / {num2}. A variavelExemplo ao final possuirá o valor {num1 / num2}")
                ObjOpAtribuicao.opAtribuicao()
            elif escolhaMenu == "5":
                print("O operador vezes igual faz com que os valores da variável do lado esquerdo seja multiplicado pelo valor do lado direito e por fim reatribuído à variável\n")
                num1 = int(input("Informe um número inteiro que será o valor da variávelExemplo: "))
                num2 = int(input("Informe outro número inteiro: "))
                print(f"variavelExemplo *= {num2}, isso é o mesmo que escrever: variavelExemplo = variavelExemplo * {num2}. A variavelExemplo ao final possuirá o valor {num1 * num2}")
                ObjOpAtribuicao.opAtribuicao()
            elif escolhaMenu == "6":
                print("O operador módulo igual faz com que os valores da variável do lado esquerdo receba o resto da divisão pelo valor do lado direito e por fim reatribuído à variável\n")
                num1 = int(input("Informe um número inteiro que será o valor da variávelExemplo: "))
                num2 = int(input("Informe outro número inteiro: "))
                print(f"variavelExemplo %= {num2}, isso é o mesmo que escrever: variavelExemplo = variavelExemplo % {num2}. A variavelExemplo ao final possuirá o valor {num1 % num2}")
                ObjOpAtribuicao.opAtribuicao()
            elif escolhaMenu == "7":
                print("\nMelhor forma de aprender é testando!\n")
                return ""
            else:
                raise ValueError("\nInformação incorreta!")

        except ValueError as e:
            print("\nopção inexistente -", e)


ObjOpAtribuicao = OpAtribuicao()