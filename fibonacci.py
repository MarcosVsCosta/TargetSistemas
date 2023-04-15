soma = 0
valor =  int(input("Escreva um numero - "))
flag = 0
a = 0
b = 1
contador = 0

while contador < 100:
    if soma == valor :
        print ("o numero digitado pertence a sequencia")
        flag = 1
        break
    soma = a + b
    a = b
    b = soma
    contador = contador + 1
  
if flag == 0 :
    print ("o numero digitado não pertence a sequencia")
