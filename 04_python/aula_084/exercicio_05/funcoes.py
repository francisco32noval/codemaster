

def antecessor(valor):
    return valor - 1


#Funcoes Especiais
def limpar():
    if(os.name == "nt"): os.system("cls")
    else: os.system("clear")

def aguardar(tempo):
    time.sleep(tempo)