frase = input("Digite uma frase a ser invertida -  ")
A = len(frase)
contador = 0
invertida = ""

while A > 0 :
    print (frase[A-1], end="")
    A = A -1

print(invertida)

