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
