def aumentar(num):
    n = num * 1.3
    return n


def diminuir(num):
    n = num * 0.7
    return n


def dobro(num):
    n = num * 2
    return n


def metade(num):
    n = num / 2
    return n


def resumo(num):
    print('-'*30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 30)
    print(f'{"Metade:":<20}R$ {metade(num):.2f}'.replace('.', ','))
    print(f'{"Dobro:":<20}R$ {dobro(num):.2f}'.replace('.', ','))
    print(f'{"Aumento de 30%:":<20}R$ {aumentar(num):.2f}'.replace('.', ','))
    print(f'{"Diminuição de 30%:":<20}R$ {diminuir(num):.2f}'.replace('.', ','))