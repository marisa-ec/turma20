def somaDoisValores(a,b):
	return a + b

def divisaoDoisValores(a,b):
	return a/b


dec = int(input('1. Somar\n2. Dividir\n>'))
num1 = int(input('Valor do primeiro número: '))
num2 = int(input('Valor do segundo número: '))


if dec == 1:
	print("Vamos somar!")
	somaDoisValores(num1,num2)
elif dec == 2:
	print('Vamos dividir.')
	divisaoDoisValores(num1,num2)
else:
	while dec != 1 or dec != 2:
		print('digite uma opção valida')
		dec = int(input(''))

		



print(somaDoisValores(num1, num2))
