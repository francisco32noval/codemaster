import os
import time 
import globais


def candidatura():
    globais.nome 
    globais.idade
    globais.experiencia 
    limpar()
    print('A analisar')
    esperar()
    limpar()
    print('A analisar.')
    esperar()
    limpar()
    print('A analisar..')
    esperar()
    limpar()
    print('A analisar...')
    esperar()
    limpar()

    print('=== Ficha de Candidatura ===\n')
    print(f'Nome: ({globais.nome})')
    print(f'Idade: ({globais.idade})')
    print(f'Status da Candidatura: ({resultado()})')

    

def resultado():
    

    if(globais.idade < 18 and globais.experiencia.lower() == 'sim'):
        return 'APROVADO PARA A ESCOLA DE PROGRAMAÇÃO'
    elif(globais.idade < 18 and globais.experiencia.lower() == 'nao'):
        return 'NÃO APROVADO PARA A ESCOLA DE PROGRAMAÇÃO'
    elif(globais.experiencia.lower() == 'sim'):
        return 'APROVADO PARA O ESTÁGIO'
    elif(globais.experiencia.lower() == 'nao'):
        return 'NÃO APROVADO PARA O ESTÁGIO'
    else:
        return 'ERRO NOS DADOS INFORMADOS, TENTE NOVAMENTE'








#FUNCOES ESPECIAIS


def esperar():
    espera = 0.3
    time.sleep(espera)

def limpar():
    if os.name == 'nt': os.system('cls')
    else: os.system('clear')

    
