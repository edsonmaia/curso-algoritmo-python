# Aula 09 tuplas e dicionarios

# tuplas - lista imutavel
dados = (1, "Edson", 1.75, 85.5)

print(dados)
print(dados[0])
print(dados[1])
print(dados[2])
print(dados[3])

# dicionarios - objeto literal
cadastro = {
    'id': 1,
    'nome': 'Edson',
    'altura': 1.75,
    'peso': 85.5
}

print(cadastro)
print(cadastro['id'])
print(cadastro['nome'])
print(cadastro['altura'])
print(cadastro['peso'])

# cadastro['nome'] = 'Maria'
# print(cadastro['nome'])

print(cadastro.keys())
print(cadastro.values())
print(cadastro.items())

'''
Métodos para modificar dicionários:
clear(): Remove todos os itens do dicionário.
pop(key): Remove o item com a chave especificada e retorna o valor associado.
update(dict2): Atualiza o dicionário com os pares chave-valor de outro dicionário.

Outros métodos úteis:
get(key, default): Retorna o valor associado à chave, ou um valor padrão se a chave não existir.
setdefault(key, default): Se a chave não existir, adiciona-a ao dicionário com o valor padrão e retorna o valor.
copy(): Retorna uma cópia superficial do dicionário.
'''
# cadastro.clear()
# print(cadastro)
# cadastro.pop('id')
# print(cadastro)

cadastro2 = {
    'id': 2,
    'nome': 'Maria',
    'altura': 1.54,
    'peso': 52.3
}
# cadastro.update(cadastro2)
# print(cadastro)
print(cadastro.get('nome'))
print(cadastro.get('altura'))
print(cadastro.get('peso'))

cadastro.setdefault('idade', 43)
print(cadastro)
