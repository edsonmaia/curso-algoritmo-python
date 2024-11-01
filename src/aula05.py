# Aula 05 - Listas (Vetor ou Matriz)

'''
    Vetor: estrutura unidimensional, formada por posições
    Matriz: estrutura multidimensional, formada por linhas e colunas
'''
lista_de_compras = ['Arroz', 'Feijão', 'Leite', 'Ovos']

# acessar uma posição por indice
print(lista_de_compras[0])

# alterar um valor por indice
lista_de_compras[0] = 'Café' # Depois apague ou comente esta linha para acompanhar o vídeo

print(lista_de_compras[0])

# adicionar elemento no final da lista
lista_de_compras.append('Farinha')

# adicionar elemento em posição específica
lista_de_compras.insert(0, 'Suco')

# apagar último elemento da lista
lista_de_compras.pop()

# apagar elemento por índice ou posição
lista_de_compras.pop(3)

print(lista_de_compras[3])

# exibir o tamanho da lista
print(len(lista_de_compras))

# Matriz
disciplinas = [
    ['Nome', 'Disciplina'],
    ['Edson', 'Algoritmo'],
    ['Maria', 'Design']
]

print(disciplinas[-1][-1])
