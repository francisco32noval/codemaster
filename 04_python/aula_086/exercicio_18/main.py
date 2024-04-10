import funcoes
import os 
import time 


ano_corrente = int(input('- Indica o ano atual: '))
ano_nascimento = int(input('- Indica o ano de nascimento: '))


funcoes.limpar()

funcoes.analisar(0.3)

print(funcoes.getVoto(ano_corrente, ano_nascimento))


print('\n')
