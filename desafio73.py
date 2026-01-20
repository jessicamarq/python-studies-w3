#Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro, na ordem de colocação. Depois mostra:
#A-Os 5 primeiros colocados
#B-Os últimos 4 colocados
#C-Times em ordem alfabética
#D-Em que posição está o time de chapecoense

times = ('Flamengo', 'Palmeiras', 'Cruzeiro', 'Mirassol', 'Fluminense', 'Botafogo', 'Bahia', 'São Paulo', 'Grêmio', 'Bragantino', 'Atlético-MG', 'Santos', 'Corinthians', 'Vasco', 'Vitória', 'Internacional', 'Ceará', 'Fortaleza', 'Juventude', 'Sport')

print('-='*20)
print(f'Os 20 primeiros colocados do campeonato brasileiro no ano de 2025 são: \n\n{times}')
print('-='*20)
print(f'Os 5 primeiros colocados são: \n\n{times[0:5]}')
print('-='*20)
print(f'Os 4 últimos colocados são: \n\n{times[-4:]}')
print('-='*20)
print(f'A lista de time em ordem alfabética: \n\n{sorted(times)}')
print('-='*20)
print('\nChapecoense caiu para a série B, por isso não está nesta lista.\n')


