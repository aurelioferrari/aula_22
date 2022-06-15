def leiadinheiro(msg):
    while True:
        n = str(input(msg)).replace(',', '.')
        if n.isalpha() or n.strip() == '':
            print('Valor inválido.\n')
        else:
            return float(n)

