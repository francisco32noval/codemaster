import funcoes

funcoes.limpa()





opcao = None

while(opcao != 4):

    opcao = funcoes.exibirMenu()

    funcoes.limpa()

    if(opcao == 1): funcoes.getLevantamento()
    elif(opcao == 2): funcoes.getDeposito()
    elif(opcao == 3): funcoes.getPagamento()
    elif(opcao == 4): funcoes.sair()
    else:
        print('Opção Inválida!')
    


print('\n')