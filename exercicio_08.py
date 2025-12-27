valor = float(input('Digite o valor do produto para calcularmos 5% de desconto: '))
desconto = valor * 5 / 100  # quanto está sendo descontado
preco_final = valor - desconto
print(f'O desconto foi de: R${desconto:.2f}')
print(f'O valor com o desconto será: R${preco_final:.2f}')
