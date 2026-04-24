valor_total = float(input("Digite o valor total da conta: "))
# Dividir o valor total igualmente entre os três amigos
valor_por_pessoa = valor_total / 3
# Calcular quanto cada um deve pagar
carlos = int(valor_por_pessoa)
andre = int(valor_por_pessoa)
felipe = valor_total - (carlos + andre)

# Exibir quanto cada um deve pagar
print("Carlos deve pagar R$ {:.2f}".format(carlos))
print("André deve pagar R$ {:.2f}".format(andre))
print("Felipe deve pagar R$ {:.2f}".format(felipe))