# PYTHON FOR NOOBS - [EN-US](https://github.com/DjayselPessoa/projetoPFN/blob/main/README.md#python-for-noobs)

### necessário instalar o Python 3.9.6 em sua máquina! -> https://www.python.org/downloads/release/python-396/

CORRIGIDO OS NOMES DOS ARQUIVOS! PARA INICIAR O PROGRAMA UTILIZE O ARQUIVO Inicio.py

Este é um programa educativo que funciona pelo terminal com o intuito de explicar/ensinar sobre os operadores em Python para os iniciantes na linguagem.
Vale ressaltar que o maior valor educativo desta ideia É O PRÓPRIO CÓDIGO DO PROGRAMA.
O objetivo aqui é tornar essa aplicação sempre mais robusta e limpa, o que me faz ir atrás de ferramentas novas e documentação. Ver resultado é sempre animador.
O tipo de operador 'bit a bit' foi deixado de lado no momento.
Na parte sobre o programa dentro da execução do programa existem links para sites que foram utilizados como referência QUE ABRIRÃO SEU NAVEGADOR! 

NENHUM LINK É NOCIVO, MAS VERIFIQUE MESMO ASSIM!

COMO USAR:
- as opções em sua maioria são os números no começo de cada opção
- para Entrar, Criar e Sair utilize a primeira letra de cada palavra
- para opções 'A' e 'B' utilize 'a' e 'b'

IMPORTANTE:
- O arquivo inicial SAVE.csv deve conter uma linha com as Labels: COD,NOME,SENHA,SCORENAME mais uma linha em branco abaixo. 
- Essa é a única forma de fazer o programa escrever sempre abaixo da última linha e não na última linha!

Se houver Bugs reportem!

v1.0 update -> 19/01/2022
- espaços em branco nos nomes não são mais permitidos

v0.9 update -> 15/09/2021
- Correção do módulo de rank. O atributo tickTack não alternava em certo momento.
- Correção da apresentação final que impedia em certos momentos de mostrar o segundo e terceiro colocado

v0.8A update -> 14/09/2021
- Alterada a forma como termina a aplicação, salvando antes de efetuar a saida, podendo retornar ao programa ou averiguar o rank

v0.8 update -> 14/09/2021
- Utilizando sleep() para alterar a fluidez do programa.

v0.7A update -> 13/09/2021
- Agora o rank consegue obter o segundo e o terceiro lugar se houver.

v0.7 update -> 13/09/2021
- Adicionada a classe RankScore: Mostra apenas um único vencedor que no caso possuirá o maior score.
- Rank.py foi adicionado e LerScore.py foi modificado
- Inicio.py foi atualizado e exibição de texto foi modificada no processo. Alguns testes foram corrigidos.

v0.6 update -> 11/09/2021:
- Corrigido um tratamento durante o teste de senha que poderia confundir o usuário
- Corrigido o código usado para abrir o score, dependendo do ocorrido poderia não ler o score correto
- Removido código morto

v0.5 update -> 10/09/2021:
- Corrigido a falta de tratamento numa entrada que causava o término do processo e em perca de score.
- removido código morto
- Alterada a posição do texto exibido

V0.4 update -> 09/09/2021:
- Resolvido um problema com subdiretórios e pastas! Agora o processo começa no arquivo Inicio.py obtendo o Path através do import os -> pegarDirRaiz = str(os.getcwd())
- Ainda existe uma dúvida quanto a rodar no MACOS e LINUX

V0.3 update:
- Resolvida a questão do score! =]
- O programa lê CSV, atualiza criando novas linhas abaixo, gera novos arquivos SCORE.CSV para cada perfil criado.
- Alterado uma redundância com os parâmetros self.
- Correção de assuntos.

V0.2 update:
 - Acesse o programa agora pelo arquivo Opening.py
 - Necessário fazer cadastro de usuário
 - Se já houver cadastro será perguntado o que fazer.
 - Correção de assuntos

V0.1 update:
  - Adjailson me auxiliou com a organização e implementação de classes.
  - Corrigido alguns erros nos assuntos expostos.



![Image](https://mirrors.creativecommons.org/presskit/buttons/88x31/png/by-sa.png)


-----------------------------------------------------------------------------------------------------------------English

# PYTHON FOR NOOBS

### install Python 3.9.6 ->   https://www.python.org/downloads/release/python-396/

FIXED FILE NAMES! TO START THE PROGRAM USE THE FILE Inicio.py

This is an educational program that works through the terminal in order to explain/teach about Python operators for beginners in the language.
It is noteworthy that the greatest educational value of this idea is THE PROGRAM CODE ITSELF.
The goal here is to make this application ever more robust and cleaner, which makes me go after new tools and documentation. Seeing results is always encouraging.
The bitwise operator type has been left out at this time.
In the part about the program within the program execution there are links to sites that were used as a reference THAT WILL OPEN YOUR BROWSER! 

NO LINK IS HARMFUL, BUT CHECK ANYWAY!

HOW TO USE:
- the options mostly are the numbers at the beginning of each option
- to Entrar, Criar and Sair use the first letter of each word ( e, c, s )
- for options 'A' and 'B' use 'a' and 'b'

IMPORTANT:
- The initial SAVE.csv must contain a line with the Labels: COD,NOME,SENHA,SCORENAME plus a blank line below. 
- That's the only way to make the program always write below the last line and not on the last line!

If there are Bugs report!

v1.0 update -> 01/19/2022
- blank spaces in names are no longer allowed

v0.9 update -> 15/09/2021
- Fixed rank module. The tickTack attribute did not toggle at one point.
- Correction of the final presentation that prevented, at certain times, from showing the second and third place

v0.8A update -> 14/09/2021
- Changed the way the application ends, saving before exiting and being able to return to the program or check the rank

v0.8 update -> 14/09/2021
- Using sleep() to change the fluidity of the program.

v0.7A update -> 13/09/2021
- Now the rank can get the second and third place if there is.

v0.7 update -> 13/09/2021
- Added rankscore class: Shows only a single winner who in this case will have the highest score.
- Rank.py has been added and LerScore.py been modified
- Inicio.py has been updated and text display has been modified in the process. Some tests have been fixed.

v0.6 update -> 11/09/2021:
- Fixed a treatment during password testing that could confuse the user
- Fixed the code used to open the score, depending on what happened might not read the correct score
- Removed dead code

v0.5 update -> 10/09/2021:
- Fixed the lack of treatment in an entry that caused the end of the process and in loss of score.
- removed dead code
- Changed the position of the displayed text

V0.4 update -> 09/09/2021:
- Solved an issue with subdirectories and folders! Now the process starts in the Inicio.py getting the Path by: import os -> pegarDirRaiz = str(os.getcwd())
- There is still a doubt about running on MACOS and LINUX

V0.3 update:
- Solved the score issue! =]
- The program reads CSV, updates creating new lines below, generates new SCORE files. CSV for each profile created.
- Changed a redundancy with the self parameters.
- Correction of subjects.

V0.2 update:
 - Access the program now from the file Opening.py
 - Necessary to register user
 - If there is already a record, you will be asked what to do.
 - Correction of subjects

V0.1 update:
  - Adjailson assisted me with the organization and implementation of classes.
  - Fixed some errors in the subjects exposed.




![Image](https://mirrors.creativecommons.org/presskit/buttons/88x31/png/by-sa.png)

----------------------------------------------------------------------------------------------------------QRCODE to HERE


![QR](https://github.com/DjayselPessoa/projetoPFN/blob/main/SRC/qrcode_github.com.png)
