# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.

alunos = []
while True:
	nome = input('Nome: ')
	nota1 = float(input('Nota 1: '))
	nota2 = float(input('Nota 2: '))
	alunos.append([nome, [nota1, nota2], (nota1 + nota2) / 2])
	resp = input('Quer continuar? [S/N] ').strip().upper()
	if resp == 'N':
		break

print('-=' * 15)
print(f'{'No.':<4}{'NOME':<10}{'MÉDIA':>8}')
print('-' * 26)
for i, aluno in enumerate(alunos):
	print(f'{i:<4}{aluno[0]:<10}{aluno[2]:>8.1f}')

while True:
	opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
	if opc == 999:
		break
	if 0 <= opc < len(alunos):
		print(f'Notas de {alunos[opc][0]} são {alunos[opc][1]}')
print('FINALIZANDO...')