nome: input("insira o nome do aluno:") # type: ignore
nota1 = float(input("insira a primeiro nota:"))
nota2 = float(input("insira a segundo nota:"))
media = (nota1 + nota2) / 2 
print("a media das notas é: ", media)
if media >= 7:
    print("o aluno esta aprovado")
else:
    print("o aluno esta reprovado")
