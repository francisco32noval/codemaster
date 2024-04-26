import time
import os
import globals



def exibirMenu():
    animacao()
    print("=== Padaria Python ===\n")
    print("1 - Vender.")
    print("2 - Ver histórico.")
    print("0 - Sair.\n")
    return int(input("- Opção: "))



def getVenda():
    limpa()
    animacao()

    print('--- Vender ---')

    produto_vendido = str(input('- Descrição da venda: ')) 
      
    valor_venda = float(input('- Valor total da venda: '))

    if(valor_venda > 0):
        print('==== Sucesso! ====')
        globals.valor_total_vendas += valor_venda
        globals.produtos_vendidos += f'{produto_vendido} : {valor_venda}\n'
    else:
        print('--- Valor Inválido ---')
    
    carregueEnter()

def getHistorico():

    print('--- Histórico ---')

    print(f'Total das vendas: {globals.valor_total_vendas}')

    print(f'\n {globals.produtos_vendidos}')

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