qtd_frangos = int(input("Digite a quantidade de frangos"))

custo_chip = 4.0
custo_alimentos = 3.50

gasto_por_frango = custo_chip + (2 * custo_alimentos)
gasto_total = qtd_frangos * gasto_por_frango

print("A quantia de frangos na fazenda é: ", qtd_frangos)
print("Para colocar a quantidade que deseja de aneis será preciso gastar: ", gasto_total)