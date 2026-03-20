nome = input("Digite seu nome: ")
idade = int(input("digite sua idade: "))
while True:
    if idade > 120 or idade < 0:
        print("idade inválida! Por favor, digite um valor maior que 0 e menor ou igual a 120.")
        idade = int(input("digite sua idade: "))
    else:
        break
dias_de_vida = idade * 365
print(f"Olá {nome}, voce já viveu cerca de: {dias_de_vida}")