km = float(input('quantos km foram percorridos?: '))
dias = float(input('por quantos dias voce alugou o carro?: '))
valor_final = (km * 0.15) + (dias * 60)
print(f'você alugou o carro por {dias:.0f} dias e percorreu {km:.1f}km, portanto, o valor a ser pago corresponde a R${valor_final:.2f}')
