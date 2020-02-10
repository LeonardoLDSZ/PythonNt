# #---- Imprimir inifo na tela (COMENTÁRIO)
# #CTRL+K CTRL+C
# # print('\n') # pular de linha
# # print('*'*50)
# # print('Olá', 'Joelma', 'do Calypso')              
# # print('Olá' + 'Chimbinha' + 'do Calypso') 
# # print('\n')           


# Pegar entrada do usuário
nome = input('Digite seu nome: ') #ler
sobrenome = input('Digite seu sobrenome: ')


# usando a função format para concatenação de string
print('Ola {} {}'.format( nome, sobrenome))


# interpolação de strings
print( f'ola {nome} {sobrenome}')

idade =  (input('Digite a idade: '))
print (idade)
