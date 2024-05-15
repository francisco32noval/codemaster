import funcoes
from User import *


funcoes.limpa()

while(True):

    funcoes.animacao()
    print('=== Login ===\n')
    login_digitado = input('- Login: ')
    senha_digitada = input('- Senha: ')

    if funcoes.verificarLogin(login_digitado, senha_digitada):
        print('\n--- SUCESSO! ---')
        break
    else:
        print('\n--- Login INVÁLIDO! ---')
    funcoes.carregueEnter()


print('\n')