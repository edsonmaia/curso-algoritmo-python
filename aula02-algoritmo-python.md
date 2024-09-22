# Curso de Algoritmo em Python

## Aula 02 - Comando de Entrada

1. Acesse o site `https://www.onlinegdb.com/`
2. No canto superior direito em `Language`, escolha `Python 3`
3. Na área de código, apague tudo que está lá e digite o seguinte:

~~~python
# Aula 02 - Comando de entrada
nome = input('Digite o seu nome: ')

# Comando de saida
print("Nome:", nome)

~~~

## Comando de entrada

No python o comando de entrada é a função `input()`

Entre os parênteses digitamos a mensagem de interação a ser exibida para o usuário.

> A mensagem pode ser digitada entre aspas ou entre apóstrofes, ou mesmo pode ser uma variável, sem aspas ou apóstrofes.

## Como executar o código

1. Clique no botão `Run` ou tecla `F9`.
2. Na parte inferior da tela, está o Terminal ou Console, nele irá aparecer o resultado da execução do código.

## Conversão de tipos

Toda vez que recebemos um conteúdo usando a função `input()` do python recebemos um dado do tipo String ou str.

Caso, você precise receber um número inteiro, decimal ou dado lógico, é necessário fazer a conversão para o tipo desejado. Veja os exemplos no código abaixo:

~~~python
nome = input("Digite o seu nome: ")
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
tem_cnh = bool(input("Tem CNH? "))

print("Nome: ", nome)
print("Idade: ", idade, "anos")
print("Altura: ", altura, "m")
print("Peso: ", peso, "kg")
print("Tem CNH? ", tem_cnh)

~~~

> Nos três exemplos acima, temos a conversão de dados do input, no caso de String, para os tipos int (números inteiro), float (números decimais) e bool (dados lógicos ou booleanos).

Execute o código e veja os resultados em tela.

## Considerações

Nesta aula vimos o comando de entrada de dados, e como fazer o procedimento de conversão de tipos. Além de parender como trabalhar com os comandos de entrada e saída em Algoritmos e programação utilizando a linguagem Python 3.x.

Salve Devs, até as próximas!
