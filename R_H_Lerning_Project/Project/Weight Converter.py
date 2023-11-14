# Weight Converter
# ^^ First Project (1)
# ^ include all we learn until new.

# My Solution
weight = input("Weight ? ")
unit = input("(L)bs or (K)g ? ")

if unit.upper() == 'K':
    print(f'your weight is >> {int(weight) * 0.45} Kilos')
elif unit.upper() == 'L':
    print(f'yor weight is >> {int(weight) / 0.45} Pounds')
else:
    print("you don't enter the correct unit")

# The Instruction Solution
weight1 = int(input("Weight ? "))
unit1 = input("(L)bs or (K)g ? ")

if unit1.upper() == 'K':
    converted = weight1 * 0.45
    print(f'you are {converted} kilos')
elif unit1.upper() == 'L':
    converted = weight1 / 0.45
    print(f'you are {converted} pounds')
