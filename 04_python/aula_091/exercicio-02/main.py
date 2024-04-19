import time
import os
import funtcion


funtcion.limpar()

carta = input('- Desejas tirar a carta de condução? ')

if(carta.lower() == 'sim'):

    teste = ''
    tentativa = 0

    while(teste.lower() != 'sim'):
        tentativa += 1
        print(f'Estudar para o teste ({tentativa}º).\n')
        teste = input(f'Passaste no ({tentativa}º) teste? ')  
        

    print(f'\nParabéns \nFoste aprovado no ({tentativa}º) teste')
    
    
else:
    print('Usa transportes públicos')


print('\n')