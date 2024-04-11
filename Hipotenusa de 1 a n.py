import math

# Pedindo um numero pro usuario
n = int(input("Digite um numero:"))

for hipotenusa in range (0, n ): # contando os valores da hipotenusa
    for cateto1 in range (1, hipotenusa): # contando o cateteto1
        for cateto2 in range (cateto1, hipotenusa): # contando o cateto2
            if cateto1 ** 2 + cateto2 ** 2 == hipotenusa ** 2:
                print("A Hipotenusa é", hipotenusa, "e os catetos são", cateto1,"e",cateto2)


