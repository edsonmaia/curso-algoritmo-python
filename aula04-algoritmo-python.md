# Curso de Algoritmo em Python

## Aula 04 - Estruturas - Estruturas Condicionais

1. Acesse o site `https://www.onlinegdb.com/`
2. No canto superior direito em `Language`, escolha `Python 3`
3. Na área de código, apague tudo que está lá e digite o seguinte:

Inicialmente, é importante alinhamos alguns conceitos. Estamos aprendendo a programar utilizando um paradigma chamado Programação Imperativa que é sequencial e estruturada. Esta forma de programação é formada basicamente por 3 partes. Em seguida estudaremos outros operadores e sua aplicação em estruturas.

~~~python
# Aula 04 - Estruturas
'''
Programação Imperativa
1. Sequência
2. Desvio Condicional ou Decisão
   if else | match case
3. Iteração - Laços de repetição ou loop
    for e while

Operadores Relacionais:
    == igual
    != diferente
    >  maior que
    <  menor que
    >= maior ou igual
    <= menor ou igual

Operadores Lógicos:
    and E
    or  OU
    not NÃO
'''

~~~

Já trabalhamos com sequências e vamos trabalhar frequentemente com esta forma de programação. Agora precisamos aprender sobre Estruturas de Controle.

## Estrutura de Devio Condicional

Em linguagem natural utilizamos uma estrutura de desvio condicional chamada `se ... senão`. Em inglês e em outras linguagens de programação esta estrutura é conhecida como `if ... else`. Faça os seguintes códigos abaixo:

~~~python
'''
    Estrutura de controle de Desvio condicional
    se senão então  if else
    notas 0 a 10
    se a nota final for maior ou igual a 7 entao aprovado
    senão
    se a nota for menor do que 7 e maior ou igual a 5 entao recuperação
    se a nota for menor do que 5 entao reprovado
'''

# if simples

nota = 7

if nota >= 7:
    print("Aprovado(a)")

# if else

nota = 6.9

if nota >= 7:
    print("Aprovado(a)")
else:
    print("Reprovado(a)")

# if elif else - if aninhado

nota = 5

if nota >= 7:
    print("Aprovado(a)")
elif nota < 7 and nota >= 5:
    print("Recuperação")
else:
    print("Reprovado(a)")

# if elsi else - if aninhado - ordem diferente de condições

nota = 7

if nota < 5:
    print("Reprovado(a)")
elif nota >= 7:
    print("Aprovado(a)")
else:
    print("Recuperação")

~~~

Execute o código e veja os resultados em tela.

> Observe que para trabalhar com a estrutura if else precisamos conhecer de comparações lógicas. Entender o problema e ver quais são as condições lógicas possíveis, só depois é que vamos utilizar a estrutura condicional para criar um desvio condicional nas nossas sequências de instruções.

## Considerações

Nesta aula vimos o que é programação imperativa, sequencial e estruturada. Aprendemos quais são os outros operadores que podemos utilizar, bem como aprendemos como trabalhar com Estruturas de Desvio Condicional em Algoritmos e programação utilizando a linguagem Python 3.x.

Salve Devs, até as próximas!
