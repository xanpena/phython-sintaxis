# -+- coding: utf-8 -*-

import random
from time import sleep

LISTA_ORDENADA = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '#', '$', '%', '&', '/', '(', ')', '=', '?', '¿']

def desordenar_letras(l1):
	LISTA_DESORDENADA = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '!', '#', '$', '%', '&', '/', '(', ')', '=', '?', '¿']
	KEYS = {}
	for i in l1:
		if i == ' ':
			ran = ' '
		else:
			ran = random.choice(LISTA_DESORDENADA) 
			LISTA_DESORDENADA.remove(ran)

		KEYS[i] = ran
		
	return KEYS

def cypher(m, k):
	words = m.split(' a ')
	cypher_message = []
	for word in words:
		cypher_word = ''
		for letter in word:
			cypher_word += k[letter]

		cypher_message.append(cypher_word)

	return' '.join(cypher_message)

def decypher(m, k):
	words = m.split(' ')
	decypher_message = []

	for word in words:
		decypher_word = ''

		for letter in word:

			for key_value, value in k.items():
				if value == letter:
					decypher_word += key_value

		decypher_message.append(decypher_word)
	return' '.join(decypher_message)



def run():
	key = desordenar_letras(LISTA_ORDENADA)
	while True:
		sleep(0.6)
		command = input(''' * --- * --- * --- * --- * --- * --- * --- * --- * --- * --- * --- * --- *
	BIENVENIDO A UN PROGRAMA PARA ENCRIPTAR TUS MENSAJES 

	Selecciona la opcion que deseas:

		1) Encriptar
		2) Decifrar
		3) Revolver las letras
		4) salir
	''')

		if command == 1:
			message = raw_input('Escribe lo que quieres encriptar:\n')
			cypher_message = cypher(message, key)
			sleep(0.5)
			print('Tu mensaje encriptado es: \n -----> {}' .format(cypher_message))

		elif command == 2:
			message = raw_input('Escribe lo que quieres desencriptar:\n')
			decypher_message = decypher(message, key)
			sleep(0.5)
			print('Tu mensaje desencriptado es: \n -----> {} '.format(decypher_message))

		elif command == 3:
			key = desordenar_letras(LISTA_ORDENADA)
			print('Revolviendo las palabras, por favor espere')
			sleep(0.5)

		elif command == 4:
			break

		else:
			print('Por favor selecciona una opcion valida')

if __name__ == '__main__':

	print('¡ E N C R I P T A C I O N ! \n')
	run()