import time
import os
import globals



def exibirMenu():
    animacao()
    print("=== Gestão de colaboradores ===\n")
    print("1 - Novo colaborador.")
    print("2 - Editar colaborador.")
    print("3 - Apagar colaborador.\n")
    print("4 - Listar todas os colaboradores.\n")
    print("0 - Sair.\n")
    return int(input("- Opção: "))

def getNovoColaborador():

    print('---- Novo Colaborador ----\n')
    nome = input('- Digita o NOME do(a) novo(a) colaborador(a): ')
    cargo = input('- Digita o CARGO do(a) novo(a) colaborador(a): ')
    ordenado = int(input('- Digita o ORDENADO do(a) novo(a) colaborador(a): '))

    novo_colaborador = [nome, cargo, ordenado]
    globals.total_colaboradores = novo_colaborador

    print('\n---- Sucesso! ----')

    carregueEnter()



def getEditarPessoa():
    print('---- Editar Pessoa ----')
    getLista(False)
    id = int(input('\n- Digita o id que desejas editar: '))
    
    if(id >= 0 and id < len(globals.total_colaboradores)):
        globals.total_colaboradores = input(f'- Digita o nome que irá substituir ({globals.total_colaboradores[id]})')
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
    if(com_titulo): print('---- Lista de Colaboradores ----')
    for i in range(len(globals.total_colaboradores)):
        print(f'(ID: {i}) | NOME: ({globals.total_colaboradores[0]}) | Cargo: ({globals.total_colaboradores[1]}) | Ordenado: ({globals.total_colaboradores[2]})')

    carregueEnter()


    
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