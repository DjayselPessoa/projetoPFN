from PacoteEscolha.AbrirBrowser import ObjAbrirBrowser


class SobrePrograma:

    def sobrePrograma(self, score):
        self.score = score
        try:
            escolha = ""
            print("-" * 98)
            print("\nOlá!\n","\nEspero que tenha gostado deste aplicativo PYTHON FOR NOOBS!\nEsta primeira versão é bem básica e utiliza somente o terminal para acesso.\n")
            print("Futuramente outras funcionalidades e provavelmente outra cara será dada à esse pequeno projeto.\nO objetivo deste programa é servir de consulta, mas de nenhum modo deve ser utilizado sozinho.\n")
            print("Sendo assim abaixo disponibilizo os links das fontes de onde essas informações sairam.\nPerceba também que com a evolução da linguagem algumas coisas podem deixar de funcionar como exposto aqui.\n")
            print("De todo modo agradeço sua paciência e espero que tenha gostado!\n")
            print("\nDjayselPessôa - programador/idealizador\n")
            print("-" * 98)
            print("\nhttps://stackoverflow.com/questions/22125114/how-to-insert-links-in-python\n")
            print("https://isolution.pro/pt/t/python/membership-operators-example/exemplo-de-operadores-de-associacao-python\n") 
            print("https://realpython.com/python-is-identity-vs-equality/\n")
            print("https://acervolima.com/python-3-operadores-logicos/\n")
            print("http://excript.com/python/operador-de-atribuicao-python.html\n")
            print("http://cristiancechinel.pro.br/my_files/algorithms/bookhtml/node39.html\n")
            print("https://isolution.pro/pt/t/python3/python-basic-operators/python-3-operadores-basicos\n")
            print("https://www.devmedia.com.br/operadores-no-python/40693\n")
            print("-" * 98)

            escolha = str(input("Para abrir todas as páginas acima no browser digite S. Para Voltar digite V:  "))

            if escolha in "Ss":
                ObjAbrirBrowser.abrirBrowser()
            elif escolha in "Vv":
                return self.score
            else:
                raise ValueError("Erro!")
        except ValueError as e:
            print("Dado informado incorreto!", e)


ObjSobrePrograma = SobrePrograma()
