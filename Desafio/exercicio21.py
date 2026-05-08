import math

metros_por_blusa = 120
metros_por_novelo = 125

qtd_blusas = int(input("Quantas blusas serão produzidas? "))

total_metros_necessarios = qtd_blusas * metros_por_blusa
total_novelos = math.ceil(total_metros_necessarios / metros_por_novelo)

print(f"Para produzir {qtd_blusas} blusas, você precisará comprar {total_novelos} novelos.")