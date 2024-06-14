camp = (
    'Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza',
    'Corinthians', 'Red Bull Bragantino', 'Fluminense',
    'América-MG', 'Atlético-GO', 'Santos', 'Ceará',
    'Internacional', 'São Paulo', 'Athletico-PR',
    'Cuiabá', 'Juventude', 'Grêmio', 'Bahia', 'Sport',
    'Chapecoense'
)
print(f'Os 5 primeiros colocados são: {camp[0:5]}')
print(f'Os últimos 4 colocados são {camp[16:]}')
print(f'Uma lista dos times em ordem alfabética ficaria {sorted(camp)}')
print(f'A Chapecoense está na  {camp.index('Chapecoense')+1}ª posição')

