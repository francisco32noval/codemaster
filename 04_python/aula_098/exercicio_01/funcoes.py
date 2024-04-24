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