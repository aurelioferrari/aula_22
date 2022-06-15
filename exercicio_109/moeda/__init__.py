def aumentar(num, sit=True):
    n = num * 1.3
    if sit == True:
        print(f'O preço com aumento de 30% é R$ {n:.2f}'.replace('.', ','))
    else:
        print(f'O preço com aumento de 30% é R$ {n}')


def diminuir(num, sit=True):
    n = num * 0.7
    if sit == True:
        print(f'O preço com diminuição de 30% é R$ {n:.2f}'.replace('.', ','))
    else:
        print(f'O preço com diminuição de 30% é R$ {n}')


def dobro(num, sit=True):
    n = num * 2
    if sit == True:
        print(f'O dobro do preço é R$ {n:.2f}'.replace('.', ','))
    else:
        print(f'O dobro do preço é R$ {n}')


def metade(num, sit=True):
    n = num / 2
    if sit == True:
        print(f'A metade do preço é R$ {n:.2f}'.replace('.', ','))
    else:
        print(f'A metade do preço é R$ {n}')