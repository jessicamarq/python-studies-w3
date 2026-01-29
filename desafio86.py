# Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.

matriz = [[0, 0, 0] for _ in range(3)]
for i in range(3):
	for j in range(3):
		matriz[i][j] = int(input(f'Digite um valor para [{i}, {j}]: '))

print('Matriz 3x3:')
for linha in matriz:
	for valor in linha:
		print(f'[{valor:^5}]', end='')
	print()