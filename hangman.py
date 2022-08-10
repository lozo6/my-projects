import random
import string
from words import words

def get_valid_word(words): # get a word w/o '-' or ' '
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    alphabet = set(string.ascii_uppercase)
    word_letters = set(word) # tracks letters in selected word
    used_letters = set() # tracks used letters user inputed
    lives = 7
    # user input
    while len(word_letters) > 0 and lives > 0:
        print(f'you have {lives} lives left and you have used these letters: ', ' '.join(used_letters))
        
        # tracks current word
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('current word: ', ' '.join(word_list))

        user_letter = input('guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')
            else:
                lives = lives - 1
                print(f'your letter, {user_letter} is not in the word')
        
        elif user_letter in used_letters:
            print('you have already used this letter, choose another letter')
        else:
            print('invalid letter')
    if lives == 0:
        print(f'you have died, the word was {word}')
    else:
        print(f'congrats the word was {word}')