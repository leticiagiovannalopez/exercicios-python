preço = float(input('qual é o valor do produto?: '))
desconto = preço * 10 / 100  
acrescimo = preço * 8 / 100 
preço_a_vista = preço - desconto
preço_juros = preço + acrescimo
print(f'um produto que custa R${preço}, terá um desconto de R${desconto}, totalizando R${preço_a_vista} se for pago à vista, e um acréscimo de R${acrescimo} se for no cartão de crédito, que totaliza R${preço_juros}')
