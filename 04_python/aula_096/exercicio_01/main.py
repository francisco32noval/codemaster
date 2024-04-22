import time
import os
import funcoes


funcoes.limpar()


print('==== BREAK NO While ====')

loop = 1


while (True):
    
    pergunta = input(f'- Voce deseja encerrar o loop WHILE na tentativa ({loop}/5)? ')

    if(loop <= 5 and pergunta.lower() == 'sim'):

        print('\nVocê nao ultrapassou as tentativas.')
        break

    elif(loop >= 5 and pergunta.lower() == 'nao'):
        print('\nVocê ultrapassou as tentativas.')
        break
    
    
    loop += 1

    
    



print('==== BREAK NO FOR ====')


for i in range(1, 6):
    
    pergunta = input(f'- Voce deseja encerrar o loop FOR na tentativa ({i}/5)? ')

    if(pergunta.lower() == 'sim'):

        print('\nVocê nao ultrapassou as tentativas.')
        break
    

    


print('\n')