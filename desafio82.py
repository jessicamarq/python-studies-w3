"""Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas."""

valores = []
pares = []
impares = []

while True:
  num = int(input('Digite um número: '))
  valores.append(num)
  if num % 2 == 0:
    pares.append(num)
  else:
    impares.append(num)
  resp = input('Você quer continuar? [S/N] ').strip().upper()
  if resp == 'N':
    break

print(f'\nA lista principal tem os seguintes números: {valores}')
print(f'Os valores pares são: {pares}')
print(f'Os valores impares são: {impares}')
