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

x = input('Which game would you like to play? ').lower()
while x != 'quit':
    if x == 'guess':
        guess(20)
        break
    elif x == 'computer guess':
        comp_guess(100)
        break
    elif x == 'rps':
        print(rps())
        break
    elif x == 'hangman':
        print(hangman())
        break
print(f'thank you for playing, {player}')