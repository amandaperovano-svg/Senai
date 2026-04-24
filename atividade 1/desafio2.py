contador = 1
soma = 0
while contador <= 5:
    salario = float(input(f"Digite o salário do {contador} funcionario: "))
    contador += 1
    soma+= salario
media = soma / 5
print ("A média dos salarios dos 5 funcionarios é: ", media)