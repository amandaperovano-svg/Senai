salario = float(input("Digite seu salario Atual: "))
x = salario * 0.15
aumento = salario + x
imposto = aumento * 0.08
salariofinal = aumento - imposto
print("O salario sem aumento era: ", salario)
print("O salario com aumento ficou: ", aumento)
print("Osalario final ficou: ", salariofinal)