import random

def rps():
    print("'r' for rock, 'p' for paper, 's' for scissors")
    computer = random.choice(['r', 'p', 's'])
    user = input("What is your choice? ")
    
    if user == computer:
        return "tie"

    if won(user, computer):
        return 'you won, computer chose ' + computer

    return 'you lost, computer chose ' + computer

def won(player, opponent):
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True