import time
import os



def getMedia(n1, n2):
    media = (n1 +n2) / 2
    if(media >= 6):
        return f'Aluno(a) aprovado(a) com média de ({media}).'
    else:
        return f'Aluno(a) não aprovado(a) com média de ({media}).'




def analisar(tempo):
    tempo = 0.3
    limpar()
    print('A analisar')
    esperar(tempo)
    limpar()
    print('A analisar.')
    esperar(tempo)
    limpar()
    print('A analisar..')
    esperar(tempo)
    limpar()
    print('A analisar...')
    esperar(tempo)
    limpar()

#Funcoes Especiais
def limpar():
    if(os.name == "nt"): os.system("cls")

def esperar(tempo):
    time.sleep(tempo)