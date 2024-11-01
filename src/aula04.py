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
