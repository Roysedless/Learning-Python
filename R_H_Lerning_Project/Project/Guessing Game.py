# Building a Guessing Game (Project)
# ^^ Making a Guessing Game using a while loop

import random  # import random for using his function
print('Choose a numer between 1 to 10')  # introduction to the game
secret_number = random.randint(1, 10)
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('  guess ? '))
    if guess > 10:
        print('Sorry your choosing is out of range!')
        break
    guess_count += 1
    if guess == secret_number:
        print('Congratulations, you succeed (:')
        break
else:
    print('Sorry, you failed ):')

# *break the all code (stop all)*
