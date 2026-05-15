# mostra uma mensagem inicial na tela
print("bem vindo(a) ao trabalho do grupo 3; Feito Marcelo, Amanda e Paola")

# pede ao usuário o valor do depósito
# float serve para aceitar números decimais
deposito = float(input("Digite o valor do depósito: "))

# pede a quantidade de meses
# int serve para aceitar números inteiros
meses = int(input("Insira quantos meses será aplicado: "))

# saldo começa zerado
saldo = 0

# taxa de juros de 0,5% ao mês
# porcentagem em python precisa ser decimal
taxa_juros = 0.005

# variável que guarda o total depositado sem os juros
total_depositado = 0

# for cria um laço de repetição
# range cria a sequência de números
# o programa vai repetir do mês 1 até o mês informado
for mes in range(1, meses + 1):

    # adiciona o depósito ao saldo
    saldo = saldo + deposito

    # soma quanto dinheiro foi depositado no total
    total_depositado = total_depositado + deposito

    # aplica os juros sobre o saldo
    saldo = saldo * (1 + taxa_juros)

    # mostra o saldo de cada mês
    # f permite usar variáveis dentro do print
    # :.2f mostra apenas 2 casas decimais
    print(f"Mês {mes}: R$ {saldo:.2f}")

# calcula quanto foi ganho apenas em juros
juros = saldo - total_depositado

# \n serve para quebrar linha
print(f"\nValor depositado: R$ {deposito:.2f}")

# mostra o valor ganho em juros
print(f"Juros ganhos: R$ {juros:.2f}")

# mostra o saldo final
print(f"Saldo final: R$ {saldo:.2f}")