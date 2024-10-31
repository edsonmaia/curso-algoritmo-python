# Curso de Algoritmo em Python

## Aula 12 - Módulos e Import

Nesta aula vamos aprender alguns conceitos extras sobre programação em Python.

## Módulos

Podemos colocar funções dentro de arquivos do python e assim criar módulos que podem ser utilizados em seus projetos. Para isto, precisamos fazer o import do arquivo desejado.

Ele pode ser local, ou seja, estar em alguma pasta em seu projeto, ou ser externo, neste caso está em alguma repositório online https://pypi.org/ é um repositório oficial. O Python Package Index (PyPI) é um repositório de software para a linguagem de programação Python.

## Import

Para fazer o import de um `módulo interno` precisamos utilizar a seguinte sintaxe:

~~~python

import nome_do_modulo
# ou
from nome_do_modulo import *
# ou
from nome_do_modulo import nome_da_funcao1, nome_da_funcao2

~~~

## Import de módulo local

No exemplo teremos dois arquivos `utils.py` e `main.py`

~~~python
# Arquivo utils.py

def somar(n1, n2):
    return n1 + n2

def dividir(n1, n2):
    return n1 / n2

~~~

Se tivermos um arquivo chamado utils.py que tenha uma ou mais funções, para importar temos que fazer o seguinte:

~~~python

# Arquivo main.py

import utils

print(utils.somar(10,2))

~~~

> Veja que para utilizar a função somar que está no arquivo utils.py temos que utilizar o nome do import seguindo de ponto e do nome da função.

Veja um exemplo utilizando o from ... import:

~~~python

from utils import *

print(somar(10,2))

~~~

> Veja que para utilizar a função somar que está no arquivo utils.py não precisamos utilizar o nome do import seguindo de ponto e do nome da função. O asterisco * serve para indicar que vamos importar tudo do arquivo.

## Import dos módulos os e time e exemplos' de uso

~~~python

import os
import time

def limpar_terminal():
  """Limpa a tela do terminal."""
  if os.name == 'nt':  # Se for Windows
    os.system('cls')
  else:  # Se for Linux/macOS
    os.system('clear')

# Chamando a função para limpar a tela
limpar_terminal()

while True:
    limpar_terminal()
    time.sleep(2)
    print("Olá, mundo!")
    time.sleep(2)

~~~

Para fazer o importe de um `módulo externo` precisamos, instalar o módulo utilizando o terminal com o seguinte comando:

~~~terminal

pip install nome_do_modulo

~~~

Exemplo prático da instalação da lib `numpy`:

~~~terminal

pip install numpy

~~~

Após a instalação no arquivo do python utilize os seguinte comando:

~~~python

import numpy as np

~~~

> O comando de import é o mesmo de import de módulos ou libs internas. O `as` serve para defirmos um alias ou apelido para o módulo que está sendo importado.

Outra forma de fazer o import dos módulos externos:

~~~python

# ou
from nome_do_modulo import *
from nome_do_modulo import nome_do_metodo, nome_do_metodo

~~~

## Como utilizar funções de um módulo ou lib

Para utilizar uma função de um módulo, precisamos utilizar o nome dele seguido de ponto e depois o nome da função. Por exemplo:

~~~python

import numpy as np

lista = np.array([10, 20, 30])
aleatorios = np.random.rand(5)

print(lista)
print(lista[0])
print(np.min(lista))
print(np.max(lista))
print(np.mean(lista))
print(aleatorios)

~~~

> Veja que para utilizar a função array() chamamos o np que é o apelido que demos para o módulo numpy. Em Python tudo é objeto. No caso, o numpy ou np é um objeto, e o array() é um método do objeto numpy.
 
## Pacotes

Para organizar seus projetos você pode armazenar os módulos dentro de uma pasta.

## Desinstalar um módulo

Para desinstalar um módulo externo faça o seguinte comando:

~~~terminal

pip uninstall nome_do_modulo

~~~

Exemplo prático de desinstalação da lib `numpy`:

~~~terminal

pip unistall numpy

~~~

Módulos ou libs - bibliotecas - são recursos poderesos de qualquer linguagem de programação.

O Python tem o repositório pypi.org que tem mais de 500 mil projetos e mais de 12 milhões de arquivos.

Como a utilização de módulos ou libs em seus projetos você irá ganhar tempo, ou seja, produtividade, pois, irá utilizar uma solução que já foi desenvolvida, testada e validada, cabendo a você apenas ler a documentação da lib no pypi.org.

## listar todas as bibliotecas instaladas

~~~terminal

pip list

~~~

# listar bibliotecas que voce instalou

~~~terminal

pip freeze 

~~~

> Existe somente as libs que você fez a instalação

# criar arquivo com a lista de bibliotecas instaladas no projeto

~~~terminal

pip freeze > requirements.txt

~~~

## instalar as bibliotecas descritas no requirements.txt

~~~terminal

pip install -r requirements.txt

~~~

## Considerações

Nesta aula aprendemos os conceitos necessários para fazermos o import de módulos internos ou externos, bem como fazer a instalação e desinstalação no caso de libs externas.

Salve Devs, até as próximas!
