"""Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele NÃO será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
"""
valores = []
while True:
  num = int(input('Digite um valor: '))
  if num not in valores:
    valores.append(num)
    print('Valor adicionado com sucesso!')
  else:
    print('Valor duplicado! Não pode ser adicionado.')
  resp = input('Quer continuar? [S/N] ').strip().upper()
  if resp == 'N':
    break

valores.sort()
print(f'Você digitou os valores: {valores}')