import os
import time

def getAnosEmDias(anos, meses, dias):
    idade = (anos * 365) + (meses * 30) + dias
    return idade
    




#Funcoes Especiais
def limpar():
    if(os.name == "nt"): os.system("cls")

def aguardar(tempo):
    time.sleep(tempo)