# my little game
import random

tries = 0
answer = random.randint(1, 100)
chances = 5

while tries < chances:
    print('------------------' * tries)
    guess = input('Enter an integer between 1 and 100: ')
    guess_int = int(guess)
    tries += 1
    if 1 <= guess_int <= 100:
        print(f'Trying {guess_int}')
        if guess_int == answer:
            print("Correct answer of", answer, "in ", tries, " tries")
            break
        elif guess_int > answer:
            print("Too high:", chances - tries, " tries remaining")
        elif guess_int < answer:
            print("Too low: ", chances - tries, " tries remaining")
        else:
            print("...we shouldn't be here")
    else:
        print("follow the instructions; you're done here")
        break
