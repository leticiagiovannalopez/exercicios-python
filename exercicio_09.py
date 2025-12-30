salario = float(input('qual é o sálario do funcionário?: '))
reajuste = salario + (salario * 15 / 100)
print(f'um salário de R${salario:,.2f}, com o aumento de 15%, fica: R${reajuste:,.2f}')
