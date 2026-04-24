preco_litro = float(input("Digite o preço do litro da gasolina: "))
valor_pago = float(input("Digite o valor que deseja abastecer: "))

litros = valor_pago / preco_litro

print("Você conseguiu abastecer", litros, "litros de gasolina.")