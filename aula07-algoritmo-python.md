# Curso de Algoritmo em Python

## Aula 07 - Estrutura de Repetição

1. Acesse o site `https://www.onlinegdb.com/`
2. No canto superior direito em `Language`, escolha `Python 3`
3. Na área de código, apague tudo que está lá e digite o seguinte:

Em linguagem natural a estrutura de repetição conhecidas são `para ... faça`, `enquanto ... faça`, e `faça... enquanto`, em inglês e outras linguagens são conhecidas como `for`, `while` e `do while`, mas, no Python temos só duas estruturas é o `for ... in` e `while`. Faça os seguintes códigos para exercitarmos:

~~~python
'''
    Aula 07 - Estruturas de repetição - loops   
    for in | while

    para (int i = 0 ; i <= 3; i++ ) faça
        ações a serem repetidas

'''

cores = ['Azul', 'Vermelho', 'Verde', 'Preto']

# for in | para ... faça ou para ... em
print("for\n")


# for cor in cores:
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

~~~

Execute o código e veja os resultados em tela.

## Considerações

Nesta aula vimos como trabalhar com as Estuturas de Repetição for e while no Python. Aprendemos também como trabalhar com o enumarate() e com operador de incremento.

Salve Devs, até as próximas!
