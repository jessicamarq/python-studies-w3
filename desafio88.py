# Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
# O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
# cadastrando tudo em uma lista composta.

import random

jogos = []
quant = int(input('Quantos jogos você quer que eu sorteie? '))
for i in range(quant):
	jogo = sorted(random.sample(range(1, 61), 6))
	jogos.append(jogo)

print('-=' * 10)
print(f'Sorteando {quant} jogos:')
for idx, jogo in enumerate(jogos, 1):
	print(f'Jogo {idx}: {jogo}')
print('-=' * 10)