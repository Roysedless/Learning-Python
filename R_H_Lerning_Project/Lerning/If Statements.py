# If Statements Learning (7)
# making a simple if statements >>
# ^^ if is hot
#      it's a hot day
#      drink plenty of water
#    otherwise if it's cold
#      it's cold day
#      wear warm clothes
#    otherwise
#      It's a lovely day


is_hot = True  # make a condition for hot day
is_cold = False  # making another condition for cold day

if is_hot:  # set the first if for hot day
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:  # set an else if for cold day
    print("It's a cold day")
    print("wear warm clothes")
else:  # set an else for nice day (this is the only situation we can get)
    print("It's a lovely day")
print('Enjoy your day')  # set a default message that we want to get in all situation.
