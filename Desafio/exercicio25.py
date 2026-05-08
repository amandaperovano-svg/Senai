total_refresco = float(input("Quantidade de refresco desejada (litros): "))

agua = total_refresco * 0.8  # 8 partes de 10
suco = total_refresco * 0.2  # 2 partes de 10

print(f"Para {total_refresco}L de refresco, use {agua:.2f}L de água e {suco:.2f}L de suco.")