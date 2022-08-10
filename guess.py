import random


def guess(x):
    secret_number = random.randint(1,x)
    for guesstaken in range(0,5):
        guess = int(input(f'guess a number from 1 to {x}: ')) #player inputs guess from 1 to x

        if guess > secret_number:
            print('your guess is too high')
        elif guess < secret_number:
            print('your guess is too low')
        else:
            break
    if guess == secret_number:
        print(f'congrats the number was {secret_number}')
    else:
        print(f'sorry, the number was {secret_number}')
