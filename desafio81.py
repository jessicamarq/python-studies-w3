"""Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista."""

valores = []

while True:
  num = int(input('Digite um valor: '))
  valores.append(num)
  resp = input('Você deseja continuar? [S/N] ').strip().upper()
  if resp == 'N':
    break

print(f'\nVocê digitou {len(valores)} números')
print(f'Os valores em ordem decrescente: {sorted(valores, reverse=True)}')
if 5 in valores:
  print('O número 5 está na lista!')
else:
  print('O número 5 NÃO foi encontrado na lista.')