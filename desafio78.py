"""Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas
respectivas posições na lista. 
(Note que o maior/menor pode aparecer em mais de uma posição).
"""

valores = []
for i in range(5):
  valores.append(int(input('Digite um valor: ')))

maior = max(valores)
menor = min(valores)

print(f'\nO maior valor digitado foi {maior} nas posições ', end='')
for i, j in enumerate(valores):
  if j == maior:
    print(f'{i}', end=' ')
print()

print(f'O menor valor digitado foi {menor} nas posições ', end='')
for i, j in enumerate(valores):
  if j == menor:
    print(f'{i}', end=' ')
print()