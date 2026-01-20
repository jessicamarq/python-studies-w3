#crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla

from random import randint

lista = tuple(randint(1,5) for i in range(5))
print(f'Os valores sorteados foram:\n', end='')
for i in lista:
  print(f'{i}')
print(f'\nO maior valor sorteado foi: {max(lista)}')
print(f'O menor valor sorteado foi: {min(lista)}\n')