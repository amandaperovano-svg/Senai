while True: 
    peso_prato = float(input("Digite o peso do prato (em kg): "))
    if peso_prato >=0:
        break
    print("Valor Invalido")

valor = peso_prato * 12.0 
print("O valor a pagar é: R$: ", valor)