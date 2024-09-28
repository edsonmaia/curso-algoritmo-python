# Curso de Algoritmo em Python

## Aula 10 - Funções

Nesta aula vamos aprender o que são rotinas e como implementar elas no Python.

## Rotinas

São sequências de ações a serem executadas de forma repetida no seu algoritmo, ou blocos de códigos reutilizáveis.

As rotinas são divididas em 2 tipos - procedimentos e funções.

## Procedimentos

São rotinas sem retorno. Com ou sem parâmetros.

## Funções

São rotinas com retorno. Com ou sem parâmetros.

> Em Orientação a Objetos as funções são chamadas de métodos.

No Python genericamente, tanto os procedimentos com as funções, iremos chamar de funções.

Para criar funções digite o seguinte código:

~~~python
# Aula 10 Funções

'''
def nomeDaFuncao(argumentos):
    Comandos

- def é a palavra reservada para declarar ou definir uma função em Python
- nomeDaFuncao é o identificador da função, ou seja, o seu nome
- argumentos são parâmetros usados pelas funções para receber dados externos e usar internamente em operações na função
- comandos são as ações a serem feitas pela função
* Métodos são "funções" dentro de Objetos.
'''

# Criar função sem parâmetros

# Definição da função, sem parâmetros
def olaMundo():
    print("Olá Mundo!")

# Chamada ou evocação da função
olaMundo()
olaMundo()

# Criar função com parâmetros

# Definição da função, com parâmetros
def exibeMensagem(mensagem):
    print(mensagem)

# Chamada ou evocação da função
exibeMensagem("Edson Maia")

# Criar função com retorno

# Definição da função, com retorno
def calculaMedia(n1, n2, n3):
    return (n1 + n2 + n3) / 3

# Chamada ou evocação da função
#print(f"{calculaMedia(7.5, 5.5, 4.0):.2f}")
media = calculaMedia(7.5, 5.5, 4.0)
print(f"{media:.2f}")
~~~

Funções são um recurso muito importante para organizar nosso código, reaproveitando trechos que se repetem, colocando eles na estrutura função que permite reutilizá-los quantas vezes for necssário.

> Apesar de ter usado o padrão de nomes camelCase nas funções. A comunidade Python prefere trabalhar com o padrão snake_case também para nomes de funções ou métodos.

## Considerações

Nesta aula aprendemos os conceitos de rotinas, procedimentos, funções, retorno, métodos, parâmetros ou argumentos e vimos exemplos práticos de como criar funções no Python.

Salve Devs, até as próximas!
