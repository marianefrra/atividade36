#lendo 4 notas e armazenando na lista

notas = []
for i in range(4):
    nota = float(input(f"digite a nota { i + 1}: "))
    notas.append(nota)

#exibindo as notas 

print("notas: ")
for nota in notas:
    print(nota)

#cauculando e exibindo a média

media = sum(notas) /len (notas)
print(f"média das notas {media:.2f}")