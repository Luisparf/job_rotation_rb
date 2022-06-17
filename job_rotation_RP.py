# -*- coding: utf-8 -*-


"""
1) Observe o trecho de código abaixo:

int INDICE = 13, SOMA = 0, K = 0;

enquanto K < INDICE faça

{

K = K + 1;

SOMA = SOMA + K;

}

imprimir(SOMA);



Ao final do processamento, qual será o valor da variável SOMA?
R: O valor da variável SOMA será 91

"""
print('\n\n################# questão 1 #################\n')
INDICE = 13
SOMA = 0
K = 0

while K < INDICE:
	K = K + 1
	SOMA = SOMA + K

print('Ao final do processamento, qual será o valor da variável SOMA?')
print(f'R: O valor da variável SOMA será {SOMA}')



"""
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE:

Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;"""

print('\n\n################# questão 2 #################\n')

while True:

	try:
		n = int(input("Enter with a non-negative integer: "))
		if isinstance(n, int) and n > 0:
			break
		elif n < 0:
			print('\nThe number must be a positive integer! Try again.\n')
	except ValueError:
		print('\nThe number must be a positive integer! Try again\n')

a = 1
b = 1
fibo = 1
x = 0
while fibo <= n:
	# print(fibo)
	if fibo == n:
		print(f'\n{n} belongs to the Fibonacci sequence.\n')
		x = 1
		break
	fibo = a + b
	# print(fibo)
	a = b
	b = fibo

if x == 0:
	print(f'\n{n} does not belong to the Fibonacci sequence.')



"""
3) Descubra a lógica e complete o próximo elemento:



a) 1, 3, 5, 7, ___ R:9

b) 2, 4, 8, 16, 32, 64, ____ R: 128

c) 0, 1, 4, 9, 16, 25, 36, ____ R: 49

d) 4, 16, 36, 64, ____ R: 100

e) 1, 1, 2, 3, 5, 8, ____ R: 13

f) 2,10, 12, 16, 17, 18, 19, ____ R:200



4 - Dois veículos (um carro e um caminhão) saem respectivamente de cidades opostas pela mesma rodovia. O carro de Ribeirão Preto em direção a Franca, a uma velocidade constante de 110 km/h e o caminhão de Franca em direção a Ribeirão Preto a uma velocidade constante de 80 km/h. Quando eles se cruzarem na rodovia, qual estará mais próximo a cidade de Ribeirão Preto?



IMPORTANTE:

a) Considerar a distância de 100km entre a cidade de Ribeirão Preto <-> Franca.

b) Considerar 2 pedágios como obstáculo e que o caminhão leva 5 minutos a mais para passar em cada um deles e o carro possui tag de pedágio (Sem Parar)

c) Explique como chegou no resultado.

R: Ambos estarão a 57,9 km de Ribeirão Preto pois ao se encontrarem ambos estarão no mesmo ponto com a mesma distância até Ribeirão Preto. Pela fórmula da velocidade média temos:

V1 = S1 / t e V2 = S2 / t, logo, t = S1 / V1 = S2 / V2 e S2 = 100 - S1

substituindo os valores na fórmula:

S1 / 110 = (100 - 21) / 80
80S1 = 110(100 - S1)
80(S1) = 11000 - 110S1
190S1 = 11000
S1 ≃ 57,9 KM




5) Escreva um programa que inverta os caracteres de um string.


IMPORTANTE:

a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

b) Evite usar funções prontas, como, por exemplo, reverse;
"""

print('\n\n################# questão 5 #################\n')


s = input("Enter with a string: ")
		
s = s[::-1]

print(f'reversed string: {s}')


