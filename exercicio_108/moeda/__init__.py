def aumentar(num, sit=True):
    n = num * 1.3
    if True:
        print(f'O preço com aumento de 30% é R$ {n:.2f}'.replace('.', ','))
    else:
        print(f'O preço com aumento de 30% é R$ {n}')


def diminuir(num):
    n = num * 0.7
    print(f'O preço com diminuição de 30% é R$ {n:.2f}'.replace('.', ','))


def dobro(num):
    n = num * 2
    print(f'O dobro do preço é R$ {n:.2f}')


def metade(num):
    n = num / 2
    print(f'A metade do preço é R$ {n:.2f}')