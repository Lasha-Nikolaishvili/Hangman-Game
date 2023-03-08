import random

capitals = ['tbilisi', 'berlin', 'tokyo', 'bern', 'moscow', 'amsterdam', 'athens', 'bratislava', 'bucharest'
            'kiev', 'lisbon', 'london', 'madrid', 'riga', 'paris', 'oslo', 'stockholm', 'vienna', 'vilnius']


def cal_try_cnt(diff):
    if diff == 1:
        return 20
    elif diff == 2:
        return 15
    else:
        return 10


def display_rules():
    print('The objective of this game is to guess the name of the capital.')
    print('Enter one letter at a time.')
    print('Enter -1 if you want to quit the game.')
    print('There are three difficulty levels(with different amount of allowed wrong guesses):\n'
          'Easy(20), Medium(15), Hard(10)')


display_rules()
try_count = cal_try_cnt(int(input('Select difficulty index(1 - Easy, 2 - Medium, 3 - Hard): ')))

guess = ''
random.shuffle(capitals)
hidden_word = capitals[0]
guessed_word = ''
for i in range(0, len(hidden_word)):
    guessed_word += '*'

while try_count > 0:
    print(guessed_word)
    guess = input('Enter a letter: ')
    if guess == '-1':
        print('You have quit the game :(')
        break

    for i in range(0, len(hidden_word)):
        if guess == hidden_word[i]:
            guessed_word = list(guessed_word)
            guessed_word[i] = guess
            guessed_word = ''.join(guessed_word)

    if guessed_word == hidden_word:
        print(f"You Win! The answer is {guessed_word}!")
        break

    try_count -= 1

if try_count <= 0:
    print('Your try count has run out! you lost :(')
