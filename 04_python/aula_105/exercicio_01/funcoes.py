import time
import os
import globals

def exibirMenu():
    animacao()
    print("=== Restaurante ===\n")
    print("1 - Novo colaborador.")
    print("2 - Editar colaborador.")
    print("3 - Apagar colaborador.\n")
    print("4 - Listar todas os colaboradores.\n")
    print("0 - Sair.\n")
    return int(input("- Opção: "))


def getNovoPrato():
    print('---- Novo Prato ----\n')
    nome = input('- Digita o NOME do novo prato: ')
    tempo_preparo = float(input('- Digita o TEMPO DE preparo: '))
    preco = float(input('- Digita o PREÇO de preparo: '))
    quantidade = int(input('- Digita o PREÇO de preparo: '))
    globals.cardapio.append(novoPrato(nome, tempo_preparo, preco, quantidade))
    globals.historico.append(novoHistorico(f'Registo do prato {nome}'))
    print('\n--- SUCESSO! ---')


def editarPrato():
    print('\n--- Editar prato ---')
    getListaCardapio(False)
    id = int(input('\n- Digite o ID do prato que deseja editar: '))
    if(id >= 0 and id < len(globals.cardapio)):
        print()
        exibirPrato(id)
        print('\n--- Menu de Edição ---')
        print('1 - Nome.')
        print('2 - Tempo de Preeparo.')
        print('3 - Preço.')
        print('4 - Quantidade.\n')
        print('5 - Cancelar.\n')
        opcao = int(input('- Opção: '))

        if(opcao == 1):
            globals.cardapio[id]['nome'] = input('- Digita o novo nome: ')
            print('\n--- SUCESSO! ---')
        elif(opcao == 2):
            globals.cardapio[id]['tempo_preparo'] = int(input('- Digita o tempo de preparo: '))
            print('\n--- SUCESSO! ---')
        elif(opcao == 3):
            globals.cardapio[id]['preco'] = float(input('- Digita o novo preço: '))
            print('\n--- SUCESSO! ---')
        elif(opcao == 4):
            globals.cardapio[id]['quantidade'] = int(input('- Digita a quantidade: '))
            print('\n--- SUCESSO! ---')
        elif(opcao == 5):
            print('\n--- Operação Cancelada ---')
        else:
            print('\n--- Opção Inválida ---')

    else:
        print('--- ID INVÁLIDO ---')

def apagarPrato():
    print('\n--- Apagar prato ---')
    getListaCardapio(False)
    id = int(input('\n- Digite o ID do prato que deseja apagr: '))
    if(id >= 0 and id < len(globals.cardapio)):
        print()
        exibirPrato(id)
        globals.cardapio.pop(id)
    else:
        print('ID INVÁLIDO!')



def getListaCardapio(com_titulo):
    if(com_titulo): print('=== Cardápio ===')
    for i in range(len(globals.cardapio)):
        p = globals.cardapio[1]
        print(f'#{i} - {p['nome']}  (TP: {p ['tempo_preparo']}) - (Preço: {p ['preco']}) - (Quantidade: {p ['quantidade']})')




# FUNCOES HELPERS

def novoPrato(nome, tempo_preparo, preco, quantidade):
    novo_prato = {
        'nome' : nome,
        'tempo_preparo' : tempo_preparo,
        'preco' : preco,
        'quantidade' : quantidade,
    }
    return novo_prato

def exibirPrato(id):
    p = globals.cardapio[1]
    print(f'#{id} - {p['nome']}  (TP: {p ['tempo_preparo']}) - (Preço: {p ['preco']}) - (Quantidade: {p ['quantidade']})')
    

def novoHistorico(descricao):
    novo_historico = {'descricao' : descricao}
    return novo_historico

def exibirHistorico(id):
    h = globals.historico[id]
    print(f'# {id} - {h}')


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