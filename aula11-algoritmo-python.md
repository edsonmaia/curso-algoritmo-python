# Curso de Algoritmo em Python

## Aula 11 - Solução dos Desafios

## Baixe o PDF dos Desafios

> [PDF dos Desafios](https://github.com/edsonmaia/curso-algoritmo-python/blob/main/pdf/curso-de-algoritmo-desafios-de-python-professor-edson-maia-2024.pdf)

## Desafio 1

~~~python
# Desafio 01
# print('|-----------------------|\n|--- CURSO DE PYTHON ---|\n|-----------------------|')

print('|-----------------------|')
print('|--- CURSO DE PYTHON ---|')
print('|-----------------------|')

~~~

## Desafio 2

~~~python
# Desafio 02
codigo = 1
descricao = "Notebook Core i5"
quantidade = 2
preco_unitario = 2499.99
preco_total = quantidade * preco_unitario

print("Código:", codigo)
print("Descrição:", descricao)
print("Quant.:", quantidade)
print("Preço Unitário R$", preco_unitario)
print("Preço Total R$", preco_total)

~~~

## Desafio 3

~~~python
# Desafio 03

nome = input("Digite seu nome: ")
altura = float(input("Digite sua altura "))
peso = float(input("Digite seu peso "))

print("Nome:", nome)
print("Altura:", altura, "metro")
print("Peso:", peso, "kg")

~~~

## Desafio 4

O desafio 4 é um complemento do desafio 3.

~~~python

# Desafio 04

imc = peso / (altura**2)
print(f"IMC: {imc:.2f}")

~~~

## Desafio 5

~~~python

# Desafio 05

nome = input("Digite seu nome: ")
nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))
media = (nota1 + nota2 + nota3) / 3

print(f"Nome: {nome}")
print(f"Nota 1: {nota1}")
print(f"Nota 2: {nota2}")
print(f"Nota 3: {nota3}")
print(f"Média: {media:.2f}")

~~~

## Desafio 6

O desafio 6 é um complemento do desafio 5.

~~~python
# Desafio 06

situacao1 = ''
situacao2 = ''
media = 5.0 # exemplo
if(media >= 7):
    situacao1 = "Aprovado"
else:
    situacao1 = "Reprovado"
    
print(f"Situação 1: {situacao1}")

if media >= 7:
    situacao2 = "Aprovado"
elif media < 7 and media >= 5:
    situacao2 = "Recuperação"
else:
    situacao2 = "Reprovado"

print(f"Situação 2: {situacao2}")

~~~

## Desafio 7

O desafio 7 é um complento dos desafios 3 e 4.

~~~python
# Desafio 07

nome = input("Digite seu nome: ")
altura = float(input("Digite sua altura "))
peso = float(input("Digite seu peso "))
imc = peso / (altura**2) # peso / (altura * altura)
classificacao_imc = ''

if imc <= 18.5:
    classificacao_imc = 'Abaixo do peso normal'
elif imc >= 18.5 and imc <= 24.9:
    classificacao_imc = 'Peso normal'
elif imc >= 25 and imc <= 29.9:
    classificacao_imc = 'Sobrepeso'
elif imc >= 30 and imc <= 34.9:
    classificacao_imc = 'Obesidade grau I'
elif imc >= 35 and imc <= 39.9:
    classificacao_imc = 'Obesidade grau II ou severa'
elif imc >= 40:
    classificacao_imc = 'Obesidade grau III ou mórbida'
else:
    classificacao_imc = ''

print("Nome:", nome)
print("Altura:", altura, "metro")
print("Peso:", peso, "kg")
print(f"IMC: {imc:.2f}")
print("Classificação do IMC:", classificacao_imc)

~~~

## Desafio 8

~~~python
# Desafio 08

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

for mes in meses:
    print(mes)

~~~

## Desafio 9

~~~python

# Desafio 09

sigla = input('Digite a sigla do ponto cardeal ')

match sigla:
    case 'N':
        print(f"A sigla {sigla} é do ponto cardeal Norte")
    case 'S':
        print(f"A sigla {sigla} é do ponto cardeal Sul")
    case 'W':
        print(f"A sigla {sigla} é do ponto cardeal Oeste")
    case 'O':
        print(f"A sigla {sigla} é do ponto cardeal Oeste")
    case 'E':
        print(f"A sigla {sigla} é do ponto cardeal Leste")
    case 'L':
        print(f"A sigla {sigla} é do ponto cardeal Leste")
    case _:
        print("Você só pode digitar as siglas: N, S, W ou O, E ou L")

~~~

> DICA: No input poderiamos trabalhar a função para transformar a letra para maiúscula. Ex.: variavel.upper()

## Desafio 10

~~~python

# Desafio 10

produtos = [
    ['Código', 'Produto'],
    [1, 'Arroz'],
    [2, 'Feijão'],
    [3, 'Farinha'],
]

for produto in produtos:
    print(produto)

print(f"| {produtos[0][0]}| {produtos[0][1]}")
print(f"| {produtos[1][0]}\t| {produtos[1][1]}")
print(f"| {produtos[2][0]}\t| {produtos[2][1]}")
print(f"| {produtos[3][0]}\t| {produtos[3][1]}")

~~~

## Considerações

Nesta aula vimos as soluções para os 10 desafios que foram propostos na aula 08. Você pode incrementar melhorias nos códigos utilizando os novos conceitos aprendidos, em especial o uso de funçõs.

Salve Devs, até as próximas!
