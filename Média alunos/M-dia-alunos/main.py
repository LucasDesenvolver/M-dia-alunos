n1 = float(input("Coloque a 1º nota do aluno: "))
n2 = float(input("Coloque a 2º nota: "))
n3 = float(input("Coloque a 3º nota: "))
n4 = float(input("Coloque a 4º nota: "))

soma = n1+n2+n3+n4

media = soma/4

print()

if media >= 6:
    print(f'Nota: {media}')
    print("Aprovado")

else:
    print(f'Nota: {media}')
    print("Reprovado")
