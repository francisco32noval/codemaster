from funcoes_menu import *

while(True):
    opcao = getMenu()

    limpa()
    print("###########################")
    print()

    if(opcao == 1): registar_produto()
    elif(opcao == 4): listar_produtos()
    # elif(opcao == 3): getApagarProduto()
    # elif(opcao == 4): getListarProduto(True)
    # elif(opcao == 5): getVender(True)
    # elif(opcao == 6): getListarVendas(True)
    # elif(opcao == 0): 
        # animacao("A sair")
        # break
    # else: print("--- OPÇÃO INVÁLIDA! ---")

    #carregueEnter()

    print("###########################")
    print()