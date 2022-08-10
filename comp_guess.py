import random

def comp_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low
        feedback = input(f'is the {guess} too high(H), too low (L), or correct (C): ').lower()
        if feedback == "h":
            high = guess - 1
        if feedback == "l":
            low = guess + 1
    print(f'too smart for you, number is {guess}')