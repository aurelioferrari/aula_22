import locale


def leiadinheiro(num):
    while num is not num.isnumeric():
        num = float(input('Valor inválido.\nDigite um valor em R$: ')).strip()
    else:
        return num
