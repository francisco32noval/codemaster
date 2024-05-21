import os
import time
from produto import Produto
from globals import loja

def getMenu():

    print('=== Loja Python ===')

    print('1 - Registar produto.')
    print('2 - Editar produto.')
    print('3 - Apagar produto.')
    print('4 - Listar produtos.\n')
    print('5 - Vender.')
    print('6 - Listar vendas.\n')
    print('0 - Sair.')
    return int(input('- Opção: '))



def registar_produto(): 
    print('--- Registar Produto ---')

    # 1. Buscar informações e construir objeto
    nome = input('- Digite o nome do novo produto: ')
    preco = float(input('- Digite o preco deste produto: '))
    quantidade = int(input('- Digite a quantidade deste produto: '))

    produto = Produto(nome, preco, quantidade)


    # 2. Adicionar o produto na loja
    adicionou_com_sucesso = loja.adicionar(produto)
    if adicionou_com_sucesso:
        print("Produto adicionado com sucesso!")
    else:
        print("Produto já existe.")
   

def listar_produtos():

    for produto in loja.produtos:
        print(produto.to_string())







# Helper Functions






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