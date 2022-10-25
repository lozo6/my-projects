hello = 'Hello, World!'
print(hello)
player = input('What is your name? ')
welcome = (f'hello, {player}, lets play some games!')
print(welcome)

from guess import guess
from comp_guess import comp_guess
from rps import rps
from hangman import hangman

print("""
Games:
Guess, Computer Guess, Rock, Paper, Scissors (RPS), Hangman
Quit
""")

x = ''
while x != 'quit':
    x = input('Which game would you like to play? ').lower().strip()
    if x == 'guess':
        guess(20)
        pass
    elif x == 'computer guess':
        comp_guess(100)
        pass
    elif x == 'rps':
        print(rps())
        pass
    elif x == 'hangman':
        print(hangman())
        pass
    x = input('Do you want to continue or quit? ').lower().strip()
print(f'thank you for playing, {player}')