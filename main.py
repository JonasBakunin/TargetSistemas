
import numpy as np


def fibonacci_numpy_check(num):
    # Inicializando o array de Fibonacci com dois primeiros valores
    fib_sequence = [0, 1]

    # Gerando a sequência até que o último valor seja maior ou igual ao número informado
    while fib_sequence[-1] < num:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    # Convertendo para array NumPy
    fib_array = np.array(fib_sequence)

    # Verificando se o número informado faz parte da sequência
    if num in fib_array:
        return f"O número {num} pertence à sequência de Fibonacci."
    else:
        return f"O número {num} NÃO pertence à sequência de Fibonacci."


# Exemplo de uso
numero = int(input("Digite um número:"))
print(fibonacci_numpy_check(numero))
