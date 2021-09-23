# 1 - imports - bibliotecas
import pytest


# 2 - class - classe

# 3 - definitions - definições  = métodos e funções
def print_hi(name):
    print(f'Oi, {name}')


def somar(numero1, numero2):
    return numero1 + numero2


def subtrair(numero1, numero2):
    return numero1 - numero2


def multiplicar(numero1, numero2):
    return numero1 * numero2


def dividir(numero1, numero2):
    if numero2 != 0:
        return numero1 // numero2
    else:
        return 'Não pode dividir por 0'

    # TESTE UNITÁRIO
    # TESTE DA FUNÇÃO SOMAR


def test_somar_didatico():
    # 1 - Configurar / Preparar
    numero1 = 8  # input - entrada
    numero2 = 5  # input - entrada
    resultado_esperado = 13  # output - saida
    # 2 - Executa
    resultado_atual = somar(numero1, numero2)
    # 3 - Check - Valida
    assert resultado_atual == resultado_esperado


def test_somar():
    assert somar(8, 5) == 13


def test_somar_resultado_negativo():
    assert somar(-1000, -500) == -1500


def test_subtrair():
    assert subtrair(6, 2) == 4


def test_multiolicar():
    assert multiplicar(3, 5) == 15


if __name__ == '__main__':
    print_hi('Tamara')

    resultado = somar(1, 2)
    print(f'O resulado da soma: {resultado}')

    resultado = subtrair(5, 3)
    print(f'O resulado da subtração: {resultado}')

    resultado = multiplicar(2, 4)
    print(f'O resulado da multilicação: {resultado}')

    resultado = dividir(55, 5)
    print(f'O resulado da divisão: {resultado}')
