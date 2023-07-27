# -+- coding: utf-8 -*-

def palindrome(word):
    reversed_letters = []

    for letter in word:
        reversed_letters.insert(0, letter)

    reversed_word = ''.join(reversed_letters) # word[::-1]

    if word == reversed_word:
        return True
    
    return False

if __name__ == '__main__':
    word = str(raw_input('Escribe una palabra: '))
    result = palindrome(word)

    if result == True:
        print('Es un palindromo')
    else:
        print('No es un palindromo')