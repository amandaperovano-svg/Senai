valor_tanque = int(input("digite quantos reais deseja colocar: "))
litros_totais_tanque = int(input("digite quantos litros tem o tanque: "))

valor_tanque = (valor_tanque * 7.00)
litros_totais_tanque = (valor_tanque * 7.00) + litros_totais_tanque
print("valor total que vai gastar:", valor_tanque)
print("faltam:", litros_totais_tanque, "para completar")