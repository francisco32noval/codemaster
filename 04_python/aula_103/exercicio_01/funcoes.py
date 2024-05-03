import time
import os
import globals



def exibirMenu():
    animacao()
    print("=== Cadastro de pessoas ===\n")
    print("1 - Cadastrar nova pessoa.")
    print("2 - Editar pessoa.")
    print("3 - Apagar pessoa.\n")
    print("4 - Listar todas as pessoas registadas.\n")
    print("0 - Sair.\n")
    return int(input("- Opção: "))

def getNovaPessoa():

    print('---- Cadastrar nova pessoa ----\n')
    
    globals.total_pessoas.append(input('- Digite o nome da nova pessoa: '))

    print('\n---- Sucesso! ----')

    carregueEnter()



def getEditarPessoa():
    print('---- Editar Pessoa ----')
    getLista(False)
    id = int(input('\n- Digita o id que desejas editar: '))
    
    if(id >= 0 and id < len(globals.total_pessoas)):
        globals.total_pessoas = input(f'- Digita o nome que irá substituir ({globals.total_pessoas[i]})')
        print('\n --- Sucesso! ---')
    else:
        print('Inválido!')


def getApagarPessoa():
    print('---- Apagar Pessoa ----')
    getLista(False)
    id = int(input('\n- Digita o id que desejas apagar: '))
    if(id >= 0 and id < len(globals.total_pessoas)):
        print(f'\n--- ({globals.total_pessoas[id]}) APAGADO COM SUCESSO')
        print('\n --- Sucesso! ---')
    else:
        print('Inválido!')


def getLista(com_titulo):
    if(com_titulo): print('---- Lista das pessoas cadastradas ----')
    for i in range(len(globals.total_pessoas)):
        print(f'ID: ({i}) - NOME: ({globals.total_pessoas[i]})')

#Funcoes Especiais
def limpa():
    if(os.name == "nt"): os.system("cls")
    else: os.system("clear")

def aguarde(tempo):
    time.sleep(tempo)

def animacao():
    tempo = 0.3
    limpa()
    print("Aguarde", end="", flush=True)
    aguarde(tempo)
    for i in range(3):
        print(".", end="", flush=True)
        aguarde(tempo)
    limpa()

def sair():
    tempo = 0.3
    limpa()
    print("A sair", end="", flush=True)
    for i in range(3):
        print(".", end="", flush=True)
        aguarde(tempo)
    limpa()

def carregueEnter(): input("\nCarregue <ENTER> para continuar...")