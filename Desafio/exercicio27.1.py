resultado = 1
for i in range(3):
    num = float(input(f"Digite o {i+1}º número: "))
    resultado *= num
print(f"Resultado final: {resultado}")