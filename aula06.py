#Tipos primitivos
"""
int(inteiros)
float(decimais)
str(textos/strings)
bool(booleanos-True/False)
"""
n1=int(input('Digite um valor:'))
n2=int(input('Digite outro valor:'))
s = n1 + n2
#print('A soma de entre o número',n1,'e',n2, 'da o resultado',resultado,'.') Antigo.


#O atual formato do print 
print('A soma entre {0} e {1} vale {2}'.format(n1, n2, s))

n=input('Digite algo')
print(n.isnumeric())