# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[0, 0, 0] for _ in range(3)]
for i in range(3):
	for j in range(3):
		matriz[i][j] = int(input(f'Digite um valor para [{i}, {j}]: '))

print('Matriz 3x3:')
for linha in matriz:
	for valor in linha:
		print(f'[{valor:^5}]', end='')
	print()

soma_pares = sum(valor for linha in matriz for valor in linha if valor % 2 == 0)
soma_col3 = sum(matriz[i][2] for i in range(3))
maior_linha2 = max(matriz[1])

print(f'A soma de todos os valores pares é {soma_pares}')
print(f'A soma dos valores da terceira coluna é {soma_col3}')
print(f'O maior valor da segunda linha é {maior_linha2}')