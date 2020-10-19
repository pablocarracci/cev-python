# Exercício 073 - Tuplas com Times de Futebol

from utils import posição

def main():
    times = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo',
        'Atlético Mineiro', 'Atlético-PR', 'Cruzeiro', 'Botafogo', 'Santos',
        'Bahia', 'Corinthians', 'Fluminense', 'Ceará', 'Vasco da Gama', 'Sport Recife',
        'América-MG', 'Chapecoense', 'Vitória', 'Paraná')

    print(f'Lista de times do Brasilerão: {times}')
    print(25 * '-=')
    print(f'Os 5 primeiros são {primeiros(5, times)}')
    print(25 * '-=')
    print(f'Os 4 últimos são {últimos(4, times)}')
    print(25 * '-=')
    print(f'Times em ordem alfabética: {sorted(times)}')
    print(25 * '-=')
    print(f'O Chapecoense está na {posição("Chapecoense", times)}ª posição')


def primeiros(n, lista):
    '''Retorna os n primeiros items de uma lista.'''
    return lista[:n]

def últimos(n, lista):
    '''Retorna os n últimos items de uma lista.'''
    return lista[-n:]


# -------------------------------------------
main()
