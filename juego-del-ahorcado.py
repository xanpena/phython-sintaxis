# -+- coding: utf-8 -*-
import random

IMAGES = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

WORDS = [
    'lavadora',
    'secadora',
    'murcielago',
    'pizarra',
    'programador',
    'computadora',
    'carretera',
    'silla',
    'teclado'
]

def random_word():
    global WORDS
    indice = random.randint(0, len(WORDS)-1)
    return WORDS[indice]

def display_board(hidden_word, tries):
    print(IMAGES[tries])
    print('')
    print(hidden_word)
    print('---- * ---- * ---- * ---- * ---- * ----')

def run():
    word = random_word()
    hidden_word = ['_'] * len(word)
    tries = 0

    while True:
        display_board(hidden_word, tries)
        current_letter = str(raw_input('Escoge un letra: '))

        letter_indexes= []
        for i in range(len(word)):
            if word[i] == current_letter:
                letter_indexes.append(i)
            
        if len(letter_indexes) == 0:
            tries+= 1

            if tries == 6:
                display_board(hidden_word, tries)
                print('Perdiste!')
                print('La palabra correcta era {}'.format(word))
                print('---- * ---- * ---- * ---- * ---- * ----')
                break
        else:
            for i in letter_indexes:
                hidden_word[i] = current_letter

        try:
            hidden_word.index('_')
        except ValueError:
            display_board(hidden_word, tries)
            print('Ganaste!')
            print('---- * ---- * ---- * ---- * ---- * ----')
            break

        
            

if __name__ == '__main__':
    print('J U E G O  D E L  A H O R C A D O')
    print('-' * 50)
    run()