import time
import os
import globals



    
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