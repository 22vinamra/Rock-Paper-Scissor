import random
from hangman_wrong_steps import steps
from words import words

def get_valid_words(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    
    return word.upper()

picked = get_valid_words(words)

print("The word has", len(picked), "letters")

for i in range(len(picked)):
    print('_', ' ', end='')

print()

right = ['_'] * len(picked)
wrong = []

def right_letter():
    for i in right:
        print(i, ' ', end='')
    print()

def wrong_letter():
    print("Wrong letters:", end='')
    for i in wrong:
        print(i, ' ', end='')
    print()


while True:
    guess = input("Guess a letter: ").upper()

    if guess in picked:

        index = 0
        for i in picked:
            if i == guess:
                right[index] = guess
            index = index + 1

        right_letter()
        wrong_letter()
        steps(len(wrong))

    elif guess not in picked:
        if guess in wrong:
            print("You already guessed", guess)
            wrong_letter()
        else:
            print(guess, "is not in my word")
            wrong.append(guess)
            right_letter()
            wrong_letter()
            steps(len(wrong))

    if len(wrong) > 4:
        print("Game Over")
        print("I picked", picked)
        break

    if '_' not in right:
        print("Congratulations!!! You have won the Game")
        print("I picked", picked)
        break
