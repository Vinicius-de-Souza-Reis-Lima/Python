'''def somar(a=0, b=0, c=0):
    """
    => Faz a soma de três valores e mostra o resultado na tela.
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    Função criada por Vinicius Reis
    """
    s = a + b + c
    print(f'A soma vale {s}')


somar(b=4, c=2)'''
'''def funçao():
    global n1
    n1 = 4
    print(f'N1 dentro vale {n1}')

n1 = 2
funçao()
print(f'N1 global vale {n1}')'''


'''def somar(a=0, b=0, c=0):
    """
    => Faz a soma de três valores e mostra o resultado na tela.
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    Função criada por Vinicius Reis
    """
    s = a + b + c
    return s


r1 = somar(3, 2, 5)
r2 = somar(2, 2)
r3 = somar(6)
print(f'Os resultados foram {r1}, {r2} e {r3}')'''


'''def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os valores são {f1}, {f2} e {f3}')'''


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('Não é par!')
    