import time
import os
import math


def getTriangulo():
    b = float(input('- Indica a base do triangulo: '))
    a = float(input('- Indica a altura do triangulo: '))
    t = (b * a) / 2 
    limpar()
    if(b <= 0 or a <= 0):
        print('Valores inválidos!')
    else:
        print(f'A area do teu triangulo é ({t:.2f})')


def getRetangulo():
    b = float(input('- Indica a base do retangulo: '))
    a = float(input('- Indica a altura do retangulo: '))
    ret = b * a 
    limpar()
    if(b <= 0 or a <= 0):
        print('Valores inválidos!')
    else:
        print(f'A area do teu retangulo é ({ret:.2f})')
   


def getCirculo():
    r = float(input('- Indica o raio do circulo: '))
    c = r**2 * (math.pi)  
    limpar()
    if(r <= 0):
        print('Valores inválidos!')
    else:
        print(f'A area do teu circulo é ({c:.2f})')






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