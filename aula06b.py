#Desafio 04 - Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possiveis sobre ele.

valor = input('Me informe algo:')

print('Você digitou:',valor)
print('O tipo do valor é:', type(valor))

print('É um numero?',valor.isnumeric())
print('É uma palavra?',valor.isalpha())
print('Tem número e palavras?',valor.isalnum())