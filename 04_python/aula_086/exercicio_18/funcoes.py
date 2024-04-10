import time
import os



def getVoto(ano_corrente, ano_nascimento):
    votar = ano_corrente - ano_nascimento
    if(votar >= 18):
        return 'Pode votar este ano.'
    else:
        return 'Não pode votar este ano.'




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