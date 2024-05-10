import time
import os
import globals


# Exibir Menu
def exibirMenu():
    animacao()
    print("=== Loja Python ===\n")
    print("1 - Registar produto.")
    print("2 - Editar produto.")
    print("3 - Apagar produto.\n")
    print("4 - Listar produtos.\n")
    print("5 - Vender.\n")
    print("6 - Listar Vendas.\n")
    print("0 - Sair.\n")
    return int(input("- Opção: "))


# Registar Produto
def regitarProduto():
    print("--- Registar Produto ---\n")
    produto = input('- Digite o nome do novo produto: ')
    preco = float(input('- Digite o preço deste produto: '))
    quantidade = int(input('- Digite a quantidade deste produto: '))
    globals.total_produtos.append(novoproduto(produto, preco, quantidade))
    print('\n--- Sucesso! ---')



# EDITAR PRODUTO
def editarProduto():
    print("--- Editar Produto ---\n")
    listarProduto(False)
    id = int(input('\n- Digita o id do produto que desejas editar: \n')) -1
    print(f'#{id + 1} - Nome: {globals.total_produtos[id]['produto']} (Preço: {globals.total_produtos[id]['preco']}) (Quantidade: {globals.total_produtos[id]['quantidade']})')

    if(id >= 0 and id < len(globals.total_produtos)):
        opcao = getMenuEdicao()
        print()
        if(opcao == 1):
            globals.total_produtos[id]['produto'] = input(f'- Digita o nome para substituir ({globals.total_produtos[id]['produto']}): ') 
            print('\n--- Sucesso ---') 
        elif(opcao == 2):
            globals.total_produtos[id]['preco'] = float(input(f'- Digita o preço para substituir ({globals.total_produtos[id]['preco']}): '))
            print('\n--- Sucesso ---') 
        elif(opcao == 3):
            globals.total_produtos[id]['quantidade'] = int(input(f'- Digita o preço para substituir ({globals.total_produtos[id]['quantidade']}): '))
            print('\n--- Sucesso ---') 
        elif(opcao == 0):
            print('\n--- Operação Cancelada ---')
        else:
            print('\n--- Opção Inválida! ---')
    else:
        print('\n--- ID INVÁLIDO ---')    


# APAGAR PRODUTO
def apagarProduto():
    print("--- Apagar Produto ---\n")
    listarProduto(False)
    id = int(input('\n- Digita o id do produto que desejas apagar: \n'))

    if(id >= 0 and id <= len(globals.total_produtos)):
        globals.total_produtos.pop(id)
        print('\n--- Sucesso ---')


# VENDA DE PRODUTOS
def venderProdutos():
    print("--- Vender Produto ---\n")
    listarProduto(False)
    id = int(input('\n- Digita o id do produto que desejas vender: \n')) -1
    if(id > 0 and id <= len(globals.total_produtos)):
        p = globals.total_produtos[id]
        quantidade_vender = int(input(f'\n- Digita a quantidade de ({p['produto']}) que será vendida: '))
        if(quantidade_vender > 0 and quantidade_vender <= p['quantidade']):
            vendido = p['quantidade'] - quantidade_vender
            p['quantidade'] = vendido
            globals.listar_vendas.append(venda(p['produto'], p['preco'], quantidade_vender))
            print(f'\n#{id} {p['produto']} ({p['preco']} $) * ({quantidade_vender}) = ({p['preco'] * quantidade_vender} $)')
            print('\n--- Sucesso ---')
        else:
            print('\n--- Quantidade INVÁLIDA ---')
    else:
        print('\n--- ID INVÁLIDO ---')


# LISTAR PRODUTOS
def listarProduto(com_titulo):
    if(com_titulo): print('--- Lista de produtos ---')
    for i in range(len(globals.total_produtos)):
        p = globals.total_produtos[i]
        print(f'#{i + 1} - Nome: {p['produto']} (Preço: {p['preco']:.2f}) (Quantidade: {p['quantidade']})')



# LISTAR VENDAS
def listarVendas(venda_feita):
    if(venda_feita): print('--- Lista de Vendas ---')
    for i in range(len(globals.listar_vendas)):
        v = globals.listar_vendas[i]
        print(f"Venda #{i + 1} - {v['produto']} ({v['preco']:.2f}) * ({v['quantidade']} uni.) =  ")



# FUNCOES HELPERS

def novoproduto(produto, preco, quantidade):
    novo_produto = {
        'produto' : produto,
        'preco' : preco,
        'quantidade' : quantidade
    }
    return novo_produto

def venda(produto, preco, quantidade_vender):
    venda = {
        'produto' : produto,
        'preco' : preco,
        'quantidade' : quantidade_vender
    }
    return venda

def getMenuEdicao():
    print('--- Menu de edição ---')
    print('1 - Nome.')
    print('2 - Preço.')
    print('3 - Quantidade.\n')
    print('0 - Cancelar.\n')
    return int(input('- Opção: '))

def init():
    globals.total_produtos.append(novoproduto('caderno', 2.3, 25))
    globals.total_produtos.append(novoproduto('Escova Colgate', 4.89, 15))
    globals.total_produtos.append(novoproduto('Marcador', 0.99, 40))


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