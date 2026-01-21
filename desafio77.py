"""Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais."""

palavras = (
  'banana',
  'computador',
  'python',
  'guanabara',
  'programacao',
  'desafio',
  'estudo',
  'livro',
  'internet',
  'teclado'
)
vogais = 'aeiou'
for i in palavras:
  print(f'Na palavra {i.upper()} temos:', end=' ')
  lista = []
  for j in i:
    if j in vogais:
      lista.append(j)
  print('-'.join(lista))