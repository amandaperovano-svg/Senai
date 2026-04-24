# Solicita ao usuário o dia e o mês da data
dia = int(input("Digite o dia: "))

# Enquanto o dia estiver fora do intervalo de 1 a 30, solicita novamente
while dia < 1 or dia > 30:
    print("Dia inválido. O dia deve estar entre 1 e 30.")
    dia = int(input("Digite o dia novamente: "))
mes = int(input("Digite o mês: "))
# Verifica se o mês fornecido é válido
while mes < 1 or mes > 12:
    print("Mês inválido. O mês deve estar entre 1 e 12.")
    mes = int(input("Digite o mês: "))

# Calcula quantos dias se passaram desde o início do ano
dias_passados = (mes - 1) * 30 + dia
print("Desde o início do ano, se passaram", dias_passados, "dias.")