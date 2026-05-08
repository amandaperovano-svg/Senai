# Entrada das quantidades de cada moeda
m01 = int(input("Quantidade de moedas de 1 centavo: "))
m05 = int(input("Quantidade de moedas de 5 centavos: "))
m10 = int(input("Quantidade de moedas de 10 centavos: "))
m25 = int(input("Quantidade de moedas de 25 centavos: "))
m50 = int(input("Quantidade de moedas de 50 centavos: "))
m1r = int(input("Quantidade de moedas de 1 real: "))

# Cálculo do valor total em reais
total = (m01 * 0.01) + (m05 * 0.05) + (m10 * 0.10) + (m25 * 0.25) + (m50 * 0.50) + (m1r * 1.00)

# Exibição do resultado
print(f"O valor total economizado é: R$ {total:.2f}")