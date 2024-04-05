import os
import time

def getAreaRetangulo(base, altura):
    area = base * altura
    return area





#Funcoes Especiais
def limpar():
    if(os.name == "nt"): os.system("cls")

def aguardar(tempo):
    time.sleep(tempo)