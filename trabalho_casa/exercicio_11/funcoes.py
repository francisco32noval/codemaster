import time
import os

def getSalario(salario_fixo, valor_total_vendas, carros_vendidos, valor_por_carro):
    salario_final = salario_fixo + (0.05 * valor_total_vendas) + (carros_vendidos * valor_por_carro)
    return salario_final





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