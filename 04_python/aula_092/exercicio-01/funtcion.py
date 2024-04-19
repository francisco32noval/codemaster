import time
import os




def getMultiplos(x):
    pass

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