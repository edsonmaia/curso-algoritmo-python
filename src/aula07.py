'''
    Aula 07 - Estruturas de repetição - loops   
    for in | while

    para (int i = 0 ; i <= 3; i++ ) faça
        ações a serem repetidas

'''

cores = ['Azul', 'Vermelho', 'Verde', 'Preto']

# for in | para ... faça ou para ... em
print("for\n")


for cor in cores:
    print(cor)

# while

print("\nwhile\n")

contador = 0

while contador <= 3:
    # print(cores[contador])
    #contador = contador + 1 # contador += 1
    contador += 1

# for utilizando indice, enumerate
for indice, cor in enumerate(cores):
    print(f"Índice {indice} corresponde à cor {cor}.")
