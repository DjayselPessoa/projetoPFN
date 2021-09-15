class OpAritmetico:

    def opAritmetico(self, score):
        self.score = score
        escolhaMenu = ""
        num1 = 0
        num2 = 0
        active = True
        print("-" * 99)
        while active:

            print(f"score: {self.score}\nOperadores Aritméticos:\n","\n[1] - Adição (+)\n[2] - Subtração (-)\n[3] - Multiplicação (*)\n[4] - Divisão (/)\n[5] - Divisão Inteira (//)\n[6] - Módulo (%)\n[7] - Exponenciação (**)\n[8] - Voltar\n")
            escolhaMenu = str(input("Escolha uma opção: "))

            try:
                if escolhaMenu == "1":
                    print("\nA adição junta valores de mesmo tipo. Quando com strings chama-se concatenação.\n")
                    num1 = int(input("Informe um número inteiro: "))
                    num2 = int(input("Informe outro número inteiro: "))
                    print(f"{num1} + {num2} -> ", num1 + num2)
                    print("\nAs operações básicas sem parênteses seguem prioridades específicas durante a execução.\nA prioridade da soma é igual da subtração tendo assim a menor prioridade durante a execução do cálculo.\n")
                    self.score += 1
                    raise ValueError("-" * 99)
                elif escolhaMenu == "2":
                    print("\nA subtração retira o valor da direita do valor da esquerda.\n")
                    num1 = int(input("Informe um número inteiro: "))
                    num2 = int(input("Informe outro número inteiro: "))
                    print(f"{num1} - {num2} -> ", num1 - num2)
                    print("\nA prioridade da subtração é igual a da soma, sendo computado por último.\n")
                    self.score += 1
                    raise ValueError("-" * 99)
                elif escolhaMenu == "3":
                    print("\nA multiplicação faz com que o número da esquerda seja somado por ele mesmo.\nA quantidade de vezes que isso ocorre é o número da direita.\n")
                    num1 = int(input("Informe um número inteiro: "))
                    num2 = int(input("Informe outro número inteiro: "))
                    print(f"{num1} * {num2} -> ", num1 * num2)
                    print("\nA prioridade da multiplicação é igual a da divisão e maior que a soma e subtração.\n")
                    self.score += 1
                    raise ValueError("-" * 99)
                elif escolhaMenu == "4":
                    print("\nA divisão faz com que o número da esquerda seja repartido na quantidade exata do número da direita, gerando, dependendo do caso, casas decimais.\n")
                    num1 = int(input("Informe um número inteiro: "))
                    num2 = int(input("Informe outro número inteiro: "))
                    print(f"{num1} / {num2} -> ", num1 / num2)
                    print("\nA prioridade da divisão é igual a da multiplicação e portanto maior que a soma e subtração.\n")
                    self.score += 1
                    raise ValueError("-" * 99)
                elif escolhaMenu == "5":
                    print("\nA divisão inteira faz com que o número da esquerda seja repartido na quantidade exata do número da direita, entretanto mesmo que gere casas decimais elas são ignoradas.\n")
                    num1 = int(input("Informe um número inteiro: "))
                    num2 = int(input("Informe outro número inteiro: "))
                    print(f"{num1} // {num2} -> ", num1 // num2)
                    print("\nA prioridade da divisão inteira é a mesma da divisão normal.\n")
                    self.score += 1
                    raise ValueError("-" * 99)
                elif escolhaMenu == "6":
                    print("\nO operador módulo também divide os valores, entretanto o valor obtido é o valor do resto.\n")
                    num1 = int(input("Informe um número inteiro: "))
                    num2 = int(input("Informe outro número inteiro: "))
                    print(f"{num1} % {num2} -> ", num1 % num2)
                    print("\nA prioridade do módulo é a mesma da divisão e multiplicação.\n")
                    self.score += 1
                    raise ValueError("-" * 99)
                elif escolhaMenu == "7":
                    print("\nO operador de exponenciação/potenciação multiplica o valor da esquerda por ele mesmo na quantidade de vezes do número da direita.\n")
                    num1 = int(input("Informe um número inteiro: "))
                    num2 = int(input("Informe outro número inteiro: "))
                    print(f"{num1} ** {num2} -> ", num1 ** num2)
                    print("\nA prioridade deste operador é maior de todas, desde que não tenha nada dentro de parênteses.\n")
                    self.score += 1
                    raise ValueError("-" * 99)
                elif escolhaMenu == "8":
                    print("\nlembre-se sempre de colocar espaço antes e depois de qualquer operador!\n")
                    return self.score
                else:
                    raise ValueError("\nDADO INCORRETO!")

            except ValueError as e:
                print(e)


ObjOpAritmetico = OpAritmetico()
