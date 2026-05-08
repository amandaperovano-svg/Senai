raio = float(input("Digite o raio da base (m): "))
altura = float(input("Digite a altura da caixa (m): "))

volume = 3.14159 * (raio ** 2) * altura

print(f"O volume da caixa d'água é: {volume:.2f} m³ (ou {volume*1000:.2f} litros).")