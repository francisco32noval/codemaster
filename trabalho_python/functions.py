import os
import time
from produtos import * 
from vendas import * 
import globals 


def getMenu():

    print('=== Loja Python ===')

    print('\n1 - Registar produto.')
    print('2 - Editar produto.')
    print('3 - Apagar produto.')
    print('4 - Listar produtos.\n')
    print('5 - Vender.')
    print('6 - Listar vendas.\n')
    print('0 - Sair.')
    return int(input('- Opção: '))




# REGISTAR PRODUTO
def registarProduto():

    limpa()
    print('--- Registar Produto ---\n')

    # 1. Buscar informações e construir objeto
    nome = input('- Digite o nome do novo produto: ')
    if(confirmarNome(nome) == False):
        preco = float(input('- Digite o preco deste produto: '))
        quantidade = int(input('- Digite a quantidade deste produto: '))
        globals.total_produtos.append(Produto(nome, preco, quantidade))

        print('\n--- Sucesso! ---')

    else:
        print('\n--- Produto ja existe! ---')



# EDITAR PRODUTO
def editarProduto():

    print('--- Editar Produto ---\n')

    listarProduto(False)

    id = int(input('\n- Digite o ID do produto que deseja editar: ')) - 1


    # MENU DE EDIÇÃO
    if(id >= 0 and id < len(globals.total_produtos)):

        print()
        globals.total_produtos[id].toString(id)
    
        print('\n--- Menu de Edição ---')
        print('1 - Nome.')
        print('2 - Preço.')
        print('3 - Quantidade.\n')
        print('0 - Cancelar.')
        opcao = int(input('- Opção: '))

        # MUDAR NOME
        if(opcao == 1):
            nome_antigo = globals.total_produtos[id].nome
            novo_nome = input(f'- Digita o nome para substituir ({nome_antigo}): ')
            if(confirmarNome(novo_nome) == False):
                globals.total_produtos[id].setNome(novo_nome)
                print('\n--- SUCESSO! ---')
            else:
                print('\n--- Nome ja existe! ---')

        # MUDAR PREÇO
        elif(opcao == 2):
            preco_antigo = globals.total_produtos[id].preco
            novo_preco = float(input(f'- Digita o preço para substituir ({preco_antigo}): '))
            if(novo_preco > 0):
                globals.total_produtos[id].setPreco(novo_preco)
                print('\n--- Sucesso! ---')
            else:
                print('\n--- Valor Inválido! ---')

        # MUDAR QUANTIDADE
        elif(opcao == 3):
            quantidade_antiga = globals.total_produtos[id].quantidade
            nova_quantidade = int(input(f'- Digita a quantidade para substituir ({quantidade_antiga}): '))
            if(nova_quantidade > 0):
                globals.total_produtos[id].setQuantidade(nova_quantidade)
                print('\n--- Sucesso! ---')
            else:
                print('\n--- Quantidade Inválida! ---')

        # OPERAÇÃO CANCELADA
        elif(opcao == 0): 
            print("--- OPERAÇÃO CANCELADA! ---")


        else: 
            print("--- OPÇÃO INVÁLIDA! ---")


    else:
        print('\n--- ID INVÁLIDO! ---')
    

# APAGAR PRODUTO
def apagarProduto():
    

    print('--- Apagar Produto ---\n')

    listarProduto(False)

    id = int(input('\n- Digite o ID do produto que deseja apagar: ')) - 1 

    if(id > 0 and id <= len(globals.total_produtos)):
        produto_a_apagar = globals.total_produtos.pop(id)
        print()
        produto_a_apagar.toString(id)
        print('\n--- SUCESSO! ---')
    else:
        print('\n--- ID INVÁLIDO! ---')




# LISTAR PRODUTO
def listarProduto(titulo):

    if(titulo):    
        print('--- Lista de Produtos ---\n')

    for p in range(len(globals.total_produtos)):
        globals.total_produtos[p].toString(p)



# VENDER PRODUTO
def venderProduto():
    print('--- Lista de Produtos ---\n')

    listarProduto(False)

    id = int(input('\n- Digite o ID do produto que queres vender: ')) - 1

    if(id > 0 and id <= len(globals.total_produtos)):

        quantidade = int(input('\n- Digite a quantidade deste produto: '))



# FUNÇÕES HELPERS

def init():
    globals.total_produtos.append(Produto("Lápis de cera", 3.54, 23))
    globals.total_produtos.append(Produto("Pincel", 0.99, 30))
    globals.total_produtos.append(Produto("Caderno desenho", 6.49, 6))

def confirmarNome(novo_produto):
        for p in globals.total_produtos:
            if p.nomeJaExiste(novo_produto):
                return True
        return False





#Funcoes Especiais
def limpa():
    if(os.name == "nt"): 
        os.system("cls")
    else:
        os.system("clear")


def aguarde(tempo):
    time.sleep(tempo)

def animacao(frase):
    tempo = 0.1
    limpa()
    print(frase, end="", flush=True)
    aguarde(tempo)
    for i in range(3):
        print(".", end="", flush=True)
        aguarde(tempo)
    limpa()

def carregueEnter(): input("\nCarregue <ENTER> para continuar...")