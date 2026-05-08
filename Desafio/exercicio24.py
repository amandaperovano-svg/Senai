altura_pessoa = float(input("Digite sua altura: "))
sombra_pessoa = float(input("Digite o comprimento de sua sombra: "))
sombra_predio = float(input("Digite o comprimento da sombra do predio: "))
altura_predio = (altura_pessoa *sombra_predio) / sombra_pessoa
print(f"A altura do predio é: {altura_predio} em metros")