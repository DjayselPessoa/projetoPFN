# Importa as bibliotecas necessárias para a vriação da barra de progresso -----------
from tqdm import tqdm
from time import sleep
#------------------------------------------------------------------------------------
#
#------------------------------------------------------------------------------------
# Cria a barra de progresso passando um valor "t" é é o tempo de duração do progresso
#------------------------------------------------------------------------------------
def barra_progresso(t):
    t = float(t)
    for i in tqdm(range(100)):
        sleep(t)
#----------------------------------------------------------------------------------
