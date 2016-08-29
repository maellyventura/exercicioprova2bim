inicio = eval(input("informe o valor inicial do intervalo: "))
fim = eval(input("informe o valor final do intervalo: "))
if(inicio < fim):
	auxiliar = inicio+1
	soma = 0
	while(auxiliar < fim):
		print (auxiliar)
		soma = auxiliar + soma
		auxiliar += 1
else:
	print("Valores informados inválidos")
print("o valor inicial é:", inicio)
print("o valor final é:", fim)
print("o valor da soma é:", soma)
