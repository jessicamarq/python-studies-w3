"""Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela. """

valores = []
for i in range(5):
  num = int(input(f'Digite o {i+1}° valor: '))
  if i == 0 or num > valores[-1]:
    valores.append(num)
    print('Número adicionado ao final da lista.')
  else: 
    pos = 0
    while pos < len(valores):
      if num <= valores[pos]:
        valores.insert(pos, num)
        print(f'Número adicionado na posição {pos}')
        break
      pos+=1

print(f'Os valores digitados em ordem foram: {valores}')