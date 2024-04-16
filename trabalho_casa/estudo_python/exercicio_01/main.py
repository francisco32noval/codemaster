import time
import os
import functions

functions.limpar()

a = float(input('- Indica a nota da primeira avaliação: '))
b = float(input('- Indica a nota da segunda avaliação: '))
c = float(input('- Indica a nota da terceira avaliação: '))

functions.limpar()

functions.analisar(0.3)

functions.limpar()

print(f'A media é ({functions.getMedia(a, b, c):.2f})')