import os
import time 



def candidatura():
    nome 
    idade
    experiencia 
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
    print(f'Nome: ({nome})')
    print(f'Idade: ({idade})')
    print(f'Status da Candidatura: ({resultado()})')

    

def resultado():
    

    if(idade < 18 and experiencia.lower() == 'sim'):
        return 'APROVADO PARA A ESCOLA DE PROGRAMAÇÃO'
    elif(idade < 18 and experiencia.lower() == 'nao'):
        return 'NÃO APROVADO PARA A ESCOLA DE PROGRAMAÇÃO'
    elif(idade >= 18 and experiencia.lower() == 'sim'):
        return 'APROVADO PARA O ESTÁGIO'
    elif(idade >= 18 and experiencia.lower() == 'nao'):
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

    
