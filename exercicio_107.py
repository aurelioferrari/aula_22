# criar módulo chamado moeda.py
# funções aumentar(), diminuir(), dobro() e metade()
# importar isso num programa e usar

import moeda

preco = float(input('Digite o preço em R$: '))
print(f'O preço com aumento de 30% é R$ {moeda.aumentar(preco):.2f}.')
print(f'O preço com diminuição de 30% é R$ {moeda.diminuir(preco):.2f}.')
print(f'O dobro do preço é R$ {moeda.dobro(preco):.2f}.')
print(f'A metade do preço é R$ {moeda.metade(preco):.2f}')
