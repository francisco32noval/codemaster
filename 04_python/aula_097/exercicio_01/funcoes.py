import time
import os
import globals



def exibirMenu():
    animacao()
    print("=== Multibanco Python ===\n")
    print("Conta: Francisco Noval")
    print(f"Slado: {globals.saldo:.2f}\n")
    print("1 - Levantamento.")
    print("2 - Depósitos.")
    print("3 - Pagamentos.\n")
    print("4 - Sair.\n")
    return int(input("- Opção: "))



def getLevantamento():
    limpa()

    print('--- Levantamentos ---\n')

    levantar = float(input('- Valor a ser levantado? '))

    if(levantar <= globals.saldo and levantar > 0):
        globals.saldo -= levantar
        globals.historico -= f'Levantamento de {levantar}'
        print('--- Sucesso ---')
    else:
        print('--- Valor Inválido ---')
        globals.historico -= f'Tentativa de levantamento de {levantar}'

    carregueEnter()

def getPagamento():
    limpa()

    print('--- Pagamentos ---\n')

    compra = input('Descrição do pagamento: ')
    pagamento = float(input('- Valor do pagamento: '))
    globals.historico -= f'Pagamento de {pagamento}'

    if(pagamento <= globals.saldo and pagamento > 0):
        globals.saldo -= pagamento
        print('--- Sucesso ---')
    else:
        print('--- Valor Inválido ---')
        globals.historico -= f'Tentativa de pagamento de {pagamento}'

    carregueEnter()


def getDeposito():
    limpa()

    print('--- Depósitos ---\n')

    depositar = float(input('- Valor a ser depositado? '))
    

    if(depositar > 0):
        globals.saldo += depositar
        print('--- Sucesso ---')
        globals.historico -= f'Deposito de {depositar}'
    else:
        print('--- Valor Inválido ---')
        globals.historico -= f'Tentativa de deposito de {depositar}'

    carregueEnter()


def getHistorico():
    print('Transações')

    print(globals.historico)




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