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
    elif(opcao == 5): funcoes.getHistorico()
    else:
        print('Opção Inválida!')
    


print('\n')