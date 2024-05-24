from functions import *
from produtos import *


limpa()

init()

while(True):
    
    
    opcao = getMenu()

    limpa()

    if(opcao == 1): registarProduto()
    if(opcao == 2): editarProduto()
    elif(opcao == 3): apagarProduto()
    elif(opcao == 4): listarProduto(True)
    # elif(opcao == 5): getVender(True)
    # elif(opcao == 6): getListarVendas(True)
    # elif(opcao == 0): 
        # animacao("A sair")
        # break
    # else: print("--- OPÇÃO INVÁLIDA! ---")

    carregueEnter()