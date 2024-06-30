import os

def load_high_score():
    if os.path.exists('high_score.txt'):
        with open('high_score.txt', 'r') as file:
            return int(file.read())
    return 0

def save_high_score(score):
    with open('high_score.txt', 'w') as file:
        file.write(str(score))
