import funcoes

funcoes.limpa()


opcao = None


while(opcao != 0):

    opcao = funcoes.exibirMenu()

    funcoes.limpa()

    if(opcao == 1): funcoes.getVenda()
    elif(opcao == 2): funcoes.getHistorico()
    elif(opcao == 0): funcoes.sair()
    else:
        print('Opção Inválida!')
    


print('\n')