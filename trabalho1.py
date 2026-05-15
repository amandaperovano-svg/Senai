print("Bem-vindo(a) ao trabalho do Grupo 3")
print("Feito por Marcelo, Amanda e Paola")

# valor fixo depositado todo mês
deposito = 1000.00

# quantidade de meses da aplicação
meses = 6

# saldo começa zerado
saldo = 0

# taxa de juros de 0,5% ao mês
taxa_juros = 0.005

# variável que guarda o total depositado sem juros
total_depositado = 0

# mostra informações iniciais
print(f"Depósito mensal: R$ {deposito:.2f}")
print(f"Tempo de aplicação: {meses} meses")
print(f"Taxa de juros: {taxa_juros * 100}% ao mês")

# laço de repetição que roda mês por mês
for mes in range(1, meses + 1):

    # adiciona o depósito ao saldo
    saldo = saldo + deposito

    # guarda quanto foi depositado sem juros
    total_depositado = total_depositado + deposito

    # aplica os juros sobre o saldo total
    saldo = saldo * (1 + taxa_juros)

    # calcula o rendimento atual
    rendimento = saldo - total_depositado

    # mostra os resultados de cada mês
    print(f"Mês {mes}")
    print(f"Saldo atual: R$ {saldo:.2f}")
    print(f"Rendimento até agora: R$ {rendimento:.2f}")

# calcula quanto foi ganho apenas em juros
juros = saldo - total_depositado

# resultados finais
print("\nResumo Final")
print(f"Total depositado: R$ {total_depositado:.2f}")
print(f"Juros ganhos: R$ {juros:.2f}")
print(f"Saldo final: R$ {saldo:.2f}")

# o f permite usar variáveis dentro do print
# \n serve para quebrar linha
# :.2f faz aparecer apenas 2 casas decimais