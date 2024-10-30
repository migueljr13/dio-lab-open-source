import math

def potencia(x, y):
    return x ** y

def raiz_quadrada(x):
    if x < 0:
        raise ValueError("Não pode calcular a raíz quadrada de um número negativo!")
    return math.sqrt(x)

def logaritimo(x, base=10):
    if x <= 0:
        raise ValueError("Entrada deve ser um valor positivo para o logarítimo!")
    return math.log(x, base)
