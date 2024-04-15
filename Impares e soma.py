import math
numero = int(input("Digite um numero:"))

contador = 1

print("Resultado para n =", numero)

for x in range(1, numero + 1):
    print("\n")
    print("O numero", x, " quando elevado ao cubo, é resultado da soma de:")
    print (x , "^", numero , "=", math.pow(x, 3))

    if x == 1:
        print(contador)
    else:

        for contador in range(contador + 2, contador + 2 * (x + 1), 2):
            print(contador, end=" ")
