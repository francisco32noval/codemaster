import main
import globais

def levantar(x):
    globais.saldo
    valor = float(input("- Digite o valor a ser levantado: "))
    if(valor <= globais.saldo and valor > 0):
        globais.saldo -= valor
    else:
        print("--- Erro ---")

def depositar(x):
    globais.saldo
    valor = float(input("- Digite o valor a ser depositado: "))
    globais.saldo += valor
    