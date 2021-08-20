def opAssociacao():
    escolhaMenu = ""
    resposta = ""
    print("---------------------------------------------------------------------------------------------------")

    print("\nEscolha abaixo qual Operador de Associação você deseja aprender:\n","\n1 - Dentro [in]\n2 - Não em [not in]\n3 - Voltar\n")
    escolhaMenu = str(input("Escolha uma opção: "))

    try:
        if escolhaMenu == "1":
            print("\nO operador de Associação [in] verifica se o valor da esquerda está contido dentro da sequência dos valores da direita. Ex.:\n")
            print("numero1 = 2, numero2 = 3, lista = [1,3,4]")
            print("A - if num1 in lista:")
            print("B - if num2 in lista:")
            resposta = str(input("Informe qual das duas opções acima A e B está correta: "))
            if resposta == "A" or resposta == "a":
                print("Resposta errada! O valor da variável numero1 não está na sequência de valores da lista.")
                opAssociacao()
            elif resposta == "B" or resposta == "b":
                print("Resposta correta! O valor da variável numero2 está na sequência de valores da lista.")
                opAssociacao()
            else:
                print("\nCaractere inválido! REINICIANDO!")
                opAssociacao()
        elif escolhaMenu == "2":
            print("\nO operador de Associação [not in] verifica se o valor da esquerda não está contido dentro da sequência dos valores da direita. Ex.:\n")
            print("numero1 = 2, numero2 = 3, lista = [1,3,4]")
            print("A - if num1 in lista:")
            print("B - if num2 in lista:")
            resposta = str(input("Informe qual das duas opções acima A e B está correta: "))
            if resposta == "A" or resposta == "a":
                print("Resposta certa! O valor da variável numero1 está na sequência de valores da lista.")
                opAssociacao()
            elif resposta == "B" or resposta == "b":
                print("Resposta incorreta! O valor da variável numero2 não está na sequência de valores da lista.")
                opAssociacao()
            else:
                print("\nCaractere inválido! REINICIANDO!")
                opAssociacao()
        elif escolhaMenu == "3":
            print("\nSempre pergunte, não aceite a dúvida!\n")
            return ""
        else:
            raise ValueError("\nInformação incorreta!")

    except ValueError as e:
        print("\nopção inexistente -", e)
