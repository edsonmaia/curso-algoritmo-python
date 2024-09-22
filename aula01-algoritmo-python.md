# Curso de Algoritmo em Python

## Aula 01 - Algoritmos e Comando de Saída

1. Acesse o site `https://www.onlinegdb.com/`
2. No canto superior direito em `Language`, escolha `Python 3`
3. Na área de código, apague tudo que está lá e digite o seguinte:

~~~python
'''
    Comentário em múltiplas linhas
    utilizando o recurso docstring do python
'''
# Comando de saida
print("Hello World")
print('Hello World!')

~~~

## Comando de saída

No python o comando de saída é a função `print()`

Entre os parênteses digitamos o conteúdo a ser escrito em tela.

Se for um texto precisa ser digitado entre aspas ou entre apóstrofes.

Se for números basta digitar diretamente os números.

Se for um dado lógico basta digitar o valor True ou False.

## Como executar o código

1. Clique no botão `Run` ou tecla `F9`.
2. Na parte inferior da tela, está o Terminal ou Console, nele irá aparecer o resultado da execução do código.

> Para dar dinamismos na programação as informações são guardada em variáveis que podem ser chamadas para ser utilizadas.

## Variáveis

São espaços na memória para armazenar determinados tipos de dados.

As variáveis tem nomes que são chamadas de `identificador`. As regras de nomes de variáveis geralmente são as seguintes:

1. Utilize letras e números
2. Utitize alguns caracteres especiais como _ - ou $
3. Use uma regra de capitulação - snake_case, camelCase, PascalCase, kebab-case, UPPERCASE.
4. No python utilizamos snake_case para nomes de variáveis.
5. Não utilize ç, letras acentuadas e alguns caracteres especiais.
6. Não utilizar palavras reservadas.

> Apesar do Python permitir nomes de variáveis com ç e letras acentudas, não utilize, para manter compatibilidade de outros projetos e linguagens.

Toda variável tem um `tipo de dados`, ou seja, é criada para armazenar um `tipo` de informação.

Quando tratamos de variáveis, existem 2 tipos de linguagens - fortemente tipadas e dinamicamente tipadas.

A linguagem Python é dinamicamente tipada. O que isto significa? Que ao criar uma variável, não precisamos indicar o tipo de dados, mas, precisamos inicializar a variável com um valor.

~~~python
# Variáveis e tipos de dados
nome = "Edson Maia"
idade = 43
altura = 1.75
peso = 85.5
tem_cnh = True

~~~

> Utilizamos o operador = para atribuir valores.

No código acima as variáveis que foram criadas receberam os valores dos principais tipos primitivos - texto, número inteiro, número real ou decimal e dados lógicos.

A variável nome é do tipo String, str ou Texto. Deve ser atribuídos entre aspas ou apóstrofes.

A variável idade é do tipo int ou Inteiro (número inteiro).

As variáveis peso e altura são do tipo float ou números reais, com pontos fluantes ou casas decimais. Usamos o . ponto como separador de casas decimais, porque as linguagens seguem o padrão americano dos EUA.

A variável tem_cnh é do tipo bool, boolean (boolenada) ou lógica. No Python só aceita os valores True (verdadeiro) ou False (falso).

## Saída de dados utilizando variáveis e textos

No primeiro código de exemplo vimos como escrever o texto "Hello World". Mas, se quisermos escrever o conteúdo de uma varíavel ou mesmo se quisermos escrever um texto concatenado com o conteúdo de variáveis temos que após declarar as varíavels fazer o seguinte:

~~~python
# Variaveis e tipos de dados
nome = "Edson Maia"
idade = 43
altura = 1.75
peso = 85.5
tem_cnh = True

# Comando de saida concatenando texto com variaveis
print("Nome:", nome)
print("Idade:", nome, "anos")
print("Altura:", nome, "metro")
print("Peso:", peso, "kg")
print("Tem CNH?:", tem_cnh)

~~~

Execute o código e veja os resultados em tela.

>> Observe que utilizamos a , vírgula para concatenar, ou seja, juntar o texto digitado entre aspas com o conteúdo das variáveis.

## Considerações

Nesta aula vimos os conceitos iniciais de Algoritmos e programação utilizando a linguagem Python 3.x.

Salve Devs, até as próximas!
