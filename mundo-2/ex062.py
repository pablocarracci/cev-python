# Exercício 062 - Super Progressão Aritmética v3.0

from utils import exibe_pa

termo_inicial = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
total_termos = quantos_termos = 10

while quantos_termos != 0:
    exibe_pa(termo_inicial, razão, quantos_termos)
    print('PAUSA')
    termo_inicial = razão * total_termos
    quantos_termos = int(input('Quantos termos você quer mostrar a mais? '))
    total_termos += quantos_termos
print(f'Progressão finalizada com {total_termos} termos mostrados.')
