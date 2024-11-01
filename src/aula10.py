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
