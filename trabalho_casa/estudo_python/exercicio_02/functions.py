import time
import os


def getHorasMinutos(minutos):
    horas = int(minutos / 60)
    resto = minutos % 60
    print(f'({minutos}) minutos equivale a ({horas}) horas e ({resto}) minutos')    






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