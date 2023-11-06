# Exercício Python 25: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas
# daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

numeros = []

for i in range(0, 6):
    numero = int(input(f'Digite o {i+1}° número: '))
    if numero % 2 == 0:
        numeros.append(numero)  # Adicione o número à lista
    soma = sum(numeros)

print(soma)