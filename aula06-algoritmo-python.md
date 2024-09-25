# Curso de Algoritmo em Python

## Aula 06 - Estruturas de Decisão

Em linguagem natural a estrutura de desvio de Decisão é conhecida como `escolha ... caso` ou `switch ... case`, mas, no Python esta estrutura é o `match ... case`. Disponível a partir da versão 3.4.

1. Acesse o site `https://www.onlinegdb.com/`
2. No canto superior direito em `Language`, escolha `Python 3`
3. Na área de código, apague tudo que está lá e digite o seguinte:

~~~python
'''
    Aula 06 - Estrutura de Decisão
    escolha caso | switch case | match case
'''
# Estrutura de Decisão match (corresponde) case (caso)

print("MENU:\n 1 - Novo \n 2 - Salvar \n 3 - Fechar")

opcao_escolhida = 1

match opcao_escolhida:
    
    case 1:
        print('Novo arquivo')
    
    case 2:
        print('Salvar arquivo')
    
    case 3:
        print('Fechar arquivo')
    
    case _:
        print('Opção inválida')

# Versão da aula com variável recebendo o valor por inpunt

'''
    Aula 06 - Estrutura de Decisão
    escolha caso | switch case | match case
'''
# Estrutura de Decisão match (corresponde) case (caso)

print("MENU:\n 1 - Novo \n 2 - Salvar \n 3 - Fechar")

opcao_escolhida = int(input("Digite o número da opção: "))

match opcao_escolhida:
    
    case 1:
        print('Novo arquivo')

    case 2:
        print('Salvar arquivo')
    
    case 3:
        print('Fechar arquivo')
    
    case _:
        print('Opção inválida')

~~~

Execute o código e veja os resultados em tela.

## Considerações

Nesta aula vimos como trabalhar com as Estuturas de Desvio de Decisão chamada match case no Python, que é equivalente à estrutura escolha caso ou switch case.

Salve Devs, até as próximas!
