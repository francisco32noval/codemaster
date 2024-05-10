import funcoes

funcoes.limpa()

funcoes.init()

while(True):

    opcao = funcoes.exibirMenu()

    funcoes.limpa()

    if(opcao == 1): funcoes.regitarProduto()
    elif(opcao == 2): funcoes.editarProduto()
    elif(opcao == 3): funcoes.apagarProduto()
    elif(opcao == 4): funcoes.listarProduto(True)
    elif(opcao == 5): funcoes.venderProdutos()
    elif(opcao == 6): funcoes.listarVendas(True)
    elif(opcao == 0): 
        funcoes.animacao('A sair')
        break
    else:
        print('Opção Inválida!')

    funcoes.carregueEnter()

print('\n')