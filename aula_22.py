def multiplica(msg):
    while True:
        n = str(input(msg)).replace(',', '.')
        if n.isalpha():
            print('Valor inválido.\n')
        else:
            return float(n)


def dobro(num):
    return num * 2


mult = multiplica('Digite um número')
dobro = dobro(mult)
print(dobro)