dias_trabalhados = int(input("Digite o número de dias trabalhados: "))

# Cálculo de anos, meses e dias
anos = dias_trabalhados // 365
meses = (dias_trabalhados % 365) // 30
dias = (dias_trabalhados % 365) % 30

# Exibição do resultado
print(f"{dias_trabalhados} dias equivalem a {anos} anos, {meses} meses e {dias} dias.")