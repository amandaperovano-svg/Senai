print("Economia para Viagem")

saldo = 1000.00
saldo_inicial = saldo
taxa_juros = 0.005
meses = 6

for mes in range(1, meses + 1):

    saldo = saldo * (1 + taxa_juros)
    lucro = saldo - saldo_inicial

    print(f"Mês {mes}: R$ {saldo:.2f}")

print(f"Saldo final: R$ {saldo:.2f}")
print(f"Lucro total: R$ {lucro:.2f}")