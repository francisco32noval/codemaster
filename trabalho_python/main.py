from functions import *
from produtos import *


limpa()

init()

while(True):
    
    
    opcao = getMenu()

    limpa()

    if(opcao == 1): 
        registarProduto()
    elif(opcao == 2): 
        editarProduto()
    elif(opcao == 3): 
        apagarProduto()
    elif(opcao == 4): 
        listarProduto(True)
    elif(opcao == 5): 
        venderProduto()
    elif(opcao == 6): 
        listarVendas()
    elif(opcao == 0): 
        animacao("A sair")
        break
    else: print("--- OPÇÃO INVÁLIDA! ---")

    carregueEnter()