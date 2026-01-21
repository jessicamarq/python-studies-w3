"""Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares."""

tupla = (int(input('Digite o 1o valor: ')),
  int(input('Digite o 2o valor: ')),
  int(input('Digite o 3o valor: ')),
  int(input('Digite o 4o valor: ')))
cont = tupla.count(9)
print(f'\nO número 9 aparece {cont} vezes')
if 3 in tupla:
  posicao = tupla.index(3)
  print(f'\nO número 3 aparece pela primeira vez na posição {posicao}')
else:
  print('O número 3 não foi digitado nenhuma vez')

print('\nOs pares são: ')
for i in tupla:
  if int(i) % 2 == 0:
    print(i, end=' ')