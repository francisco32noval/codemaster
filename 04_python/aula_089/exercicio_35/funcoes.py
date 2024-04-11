import time
import os





def getTotal(combustivel, quantidade):
    gas = quantidade * 3.30
    alc = quantidade * 2.9

    if(combustivel.lower() == 'g'):
        if(quantidade <= 20):
            return gas - (gas * 0.04)
        else:
            return gas - (gas * 0.06)
    else:
        if(quantidade <= 20):
            return alc - (alc * 0.03)
        else:
            return alc - (alc * 0.05)
        


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