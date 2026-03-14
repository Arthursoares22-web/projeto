import random


caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"


comprimento = int(input("Digite o comprimento da senha desejada: "))


senha_gerada = ""


for _ in range(comprimento):
    senha_gerada += random.choice(caracteres)


print(senha_gerada)
