# Entrada: Quantidade comprada de cada formato
qtd_lata = int(input("Quantidade de latas (350 ml): "))
qtd_600 = int(input("Quantidade de garrafas (600 ml): "))
qtd_2l = int(input("Quantidade de garrafas (2 litros): "))

# Cálculo do total de litros
# Multiplicamos cada quantidade pelo seu valor em litros
total_litros = (qtd_lata * 0.35) + (qtd_600 * 0.60) + (qtd_2l * 2.0)

# Saída do resultado
print(f"\nO total de refrigerante comprado foi de: {total_litros:.2f} litros")