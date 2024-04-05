import time
import os

distribuidor_impostos = 0.73

def getValorConsumidor(custo_fabrica):
    valor_consumidor = custo_fabrica + (distribuidor_impostos * custo_fabrica)
    return valor_consumidor



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