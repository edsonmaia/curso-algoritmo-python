# Curso de Algoritmo em Python

## Aula 03 - Operadores e Operações

1. Acesse o site `https://www.onlinegdb.com/`
2. No canto superior direito em `Language`, escolha `Python 3`
3. Na área de código, apague tudo que está lá e digite o seguinte:

~~~python
# Aula 03 - Operações

'''
    + adição
    - subtração
    * multiplicação
    / divisão
    // divisão inteira
    ** potenciação
    % modulo ou div, resto
'''
n1 = 4
n2 = 2
soma = n1 + n2
diferenca = n1 - n2
produto = n1 * n2
quociente = n1 / n2
quociente_inteiro = n1 // n2
potencia = n1 ** n2
resto = n1 % n2

print("A soma de n1 + n2 é igual a", soma)
print("A diferença de n1 - n2 é igual a", diferenca)
print("O produto de n1 * n2 é igual a", produto)
print("O quociente da divisão de n1 por n2 é igual a", quociente)
print("O quociente inteiro de n1 / n2 é igual a", quociente_inteiro)
print("A potência de n1 sobre n2 é igual a", potencia)
print("O resto da divisão de n1 por n2 é igual a", resto)
~~~

## Comando de saída usando fstring

No Python temos o `fstring` que permite fazer a formatação e concatenação da saída de textos com variáveis. Veja os exemplos do código anterior, agora utilizando o `fstring`:

~~~python

print(f"A soma de {n1} + {n2} é igual a {soma}")
print(f"A diferença de {n1} - {n2} é igual a", diferenca)
print(f"O produto de {n1} * {n2} é igual a", produto)
print(f"O quociente da divisão de {n1} por {n2} é igual a", quociente)
print(f"O quociente inteiro de {n1} / {n2} é igual a", quociente_inteiro)
print(f"A potência de {n1} sobre {n2} é igual a", potencia)
print(f"O resto da divisão de {n1} por {n2} é igual a", resto)

~~~

> Observe que utilizamos a letra f antes da abertura das aspas. Na 1ª linha mostrei como fazer o uso do fstring envolvendo todas as variáveis, perceba que elas são declaradas entre chaves {}. Nas outras linhas temos o exemplo de uso do `fstring` e a concatenação padrão usando a vírgula.

Execute o código e veja os resultados em tela.

## Considerações

Nesta aula vimos como utilizar operadores matemáticos para realizar operações em Algoritmos e programação utilizando a linguagem Python 3.x. Aprendemos também como trabalhar a saída formatada utilizando o `fstring`.

Salve Devs, até as próximas!
