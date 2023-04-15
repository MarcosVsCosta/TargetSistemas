vetor = [100,200,500,800,300]
contador = 0
escolha = "s"

while escolha == "s":
    escolha = input("Deseja incluir um valor ao vetor? [s] ou [n] ")
    if escolha.lower() == "s":
        valor = input("Digite um valor ")
        vetor.append(int(valor))
    else:
        print("\n")
   
print("menor valor do vetor: ", min(vetor))
print("maior valor do vetor: ", max(vetor))

media=sum(vetor)/len(vetor)
print ("media de valores do vetor: ", media)

for i in vetor:
    if i > media:
        contador = contador + 1

print ("existem ",contador, " valores no vetor que são maiores que a média" )
