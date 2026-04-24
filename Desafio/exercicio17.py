# Entrada: Quantidade de sanduíches
quantidade = int(input("Digite a quantidade de sanduíches: "))

# Cálculo direto (Peso em gramas convertido para quilos)
# Queijo: 2 fatias de 50g = 100g por sanduíche
queijo_kg = (quantidade * 100) / 1000

# Presunto: 1 fatia de 50g = 50g por sanduíche
presunto_kg = (quantidade * 50) / 1000

# Carne: 1 rodela de 100g = 100g por sanduíche
carne_kg = (quantidade * 100) / 1000

# Saída dos resultados
print("Para fazer", quantidade, "sanduíches, você precisa de:")
print(queijo_kg, "kg de queijo")
print(presunto_kg, "kg de presunto")
print(carne_kg, "kg de carne")