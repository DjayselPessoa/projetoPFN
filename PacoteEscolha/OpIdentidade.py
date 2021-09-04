class OpIdentidade:

    def opIdentidade(self):
        escolhaMenu = ""
        num1 = 2
        num2 = 3
        print("---------------------------------------------------------------------------------------------------")

        print("\nEscolha abaixo qual Operador de identidade você deseja aprender:\n","\n1 - É [is]\n2 - Não é [is not]\n3 - Voltar\n")
        escolhaMenu = str(input("Escolha uma opção: "))

        try:
            if escolhaMenu == "1":
                print("\nO operador de Identidade [is] a primeira vista pode parecer funcionar igual ao operador de comparação [==].\nEntretanto, enquanto [==] compara valores o operador de identidade compara se apontam para o mesmo objeto na memória.")
                print("Em suma, o operador de identidade [is] não deve ser usado para substituir o operador de comparação [==] em nenhuma circunstância. Ex.:\n")
                print("numero1 = 2", id(num1), "\nnumero2 = 3", id(num2))
                print("Acima você está vendo que numero1 contém o valor 2, entretanto o seu identificador na memória é outro valor. O mesmo para o número 2.")
                ObjOpIdentidade.opIdentidade()
            elif escolhaMenu == "2":
                print("\nO operador de Identidade [is not] também pode parecer funcionar igual ao operador de comparação [!=].\nEntretanto [!=] verifica se os valores são diferentes enquanto o operador de identidade compara se esses valores não apontam para o mesmo objeto na memória.")
                print("Em suma, o operador de identidade [is not] não deve ser usado para substituir o operador de comparação [!=] em nenhuma circunstância. Ex.:\n")
                print("numero1 = 2", id(num1), "\nnumero2 = 3", id(num2))
                print("Acima você está vendo que numero1 contém o valor 2, entretanto o seu identificador na memória é outro valor. O mesmo para o número 2.")
                ObjOpIdentidade.opIdentidade()
            elif escolhaMenu == "3":
                print("\nSempre pergunte, não aceite a dúvida!\n")
                return ""
            else:
                raise ValueError("\nInformação incorreta!")

        except ValueError as e:
            print("\nopção inexistente -", e)


ObjOpIdentidade = OpIdentidade()