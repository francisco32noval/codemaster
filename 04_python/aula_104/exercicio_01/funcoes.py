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
    globals.total_colaboradores.append(novo_colaborador)

    print('\n---- Sucesso! ----')

    carregueEnter()



def getEditarPessoa():
    print('---- Editar Pessoa ----')
    getLista(False)
    id = int(input('\n- Digita o id que desejas editar: '))



    if(id >= 0 and id < len(globals.total_colaboradores)):
        while(True):
            print('\n--- Editar ---')
            print('\n1 - Nome')
            print('\n2 - Cargo')
            print('\n3 - Ordenado')
            print('\n0 - Cancelar')

            opcao = int(input('- Opção: '))

            if(opcao == 1):
                globals.total_colaboradores[id][0] = input(f"- Digite o novo NOME que substituirá ({globals.total_colaboradores[id][0]}): ")
                print("\n--- SUCESSO! ---")
            elif(opcao == 2):
                globals.total_colaboradores[id][1] = input(f"- Digite o novo NOME que substituirá ({globals.total_colaboradores[id][1]}): ")
                print("\n--- SUCESSO! ---")
            elif(opcao == 3): 
                globals.total_colaboradores[id][2] = float(input(f"- Digite o novo NOME que substituirá ({globals.total_colaboradores[id][2]:.2f}): "))
                print("\n--- SUCESSO! ---")
            elif(opcao == 4): print("--- Operação Cancelada ---")
            else: print("--- Opção Inválida! ---")
    else:
        print('Inválido!')


def getApagarPessoa():
    print('---- Apagar Pessoa ----')
    getLista(False)
    id = int(input('\n- Digita o id que desejas apagar: '))
    if(id >= 0 and id < len(globals.total_colaboradores)):
        apagado = globals.total_colaboradores.pop(id)
        print(f"\n--- ( {apagado[0]} ) APAGADO(A) COM SUCESSO! ---")
    else:
        print('Inválido!')


def getLista(com_titulo):
    if(com_titulo): print("--- Lista dos Colaboradores ---\n")

    total_ordenado = 0

    for i in range(len(globals.total_colaboradores)):
        c = globals.total_colaboradores[i]
        print(f"(ID: {i}) | (Nome: {c[0]}) | (Cargo: {c[1]}) | (Ordenado: {c[2]:.2f} €)")
        total_ordenado += c[2]

    if(com_titulo):
        print(f"\nTotal de colaboradores: ({len(globals.total_colaboradores)})")
        print(f"Ordenado total mensal da equipa: ({total_ordenado:.2f} €)")

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