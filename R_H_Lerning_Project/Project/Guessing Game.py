# Guessing Game (Project)
# ^^ Making a Guessing Game using a while loop
print("Guess a number between 1-10: ")
number = 5
end_while = 3
guess = 11
while end_while >= 1:
    guess = int(input('Guess ? '))
    print(type(guess))
    end_round = end_while - 1

