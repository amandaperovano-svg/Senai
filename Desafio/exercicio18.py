celsius = float(input("Digite a temperatura em graus Celsius: "))

# Processamento: Aplica a fórmula de conversão
# Multiplicamos por 1.8 (que equivale à fração 9/5) e somamos 32
fahrenheit = (celsius * 1.8) + 32

# Saída: Exibe o resultado
print(f"{celsius}°C equivalem a {fahrenheit:.1f}°F")