import funcoes

funcoes.limpa()


while(True):
    opcao = funcoes.exibirMenu()

    funcoes.limpa()

    if(opcao == 1): funcoes.getNovaPessoa()
    elif(opcao == 2): funcoes.getEditarPessoa()
    # elif(opcao == 3): funcoes.getApagarPessoa()
    elif(opcao == 4): funcoes.getLista(True)
    elif(opcao == 0): 
        funcoes.animacao('A sair')
        break
    else:
        print('Opção Inválida!')


print('\n')