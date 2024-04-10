import time
import os



def getHorasJogo(fim, inicio):
    
    if(inicio == fim):
        return 'A partida teve 24h'
    elif(fim > inicio):
        return fim - inicio
    else:
        return (24 - fim) + inicio




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