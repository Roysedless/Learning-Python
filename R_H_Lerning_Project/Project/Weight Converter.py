# Weight Converter
# ^^ First Project (1)
# ^ include all we learn until new.

# My Solution
weight = input("Weight ? ")
unit = input("(L)bs or (K)g ? ")

if unit.upper() == 'K':
    print(f'your weight is >> {float(weight) / 0.45} Pounds')
elif unit.upper() == 'L':
    print(f'yor weight is >> {float(weight) * 0.45} Kilos')
else:
    print("you don't enter the correct unit")

# The Instruction Solution
weight1 = float(input("Weight ? "))
unit1 = input("(L)bs or (K)g ? ")

if unit1.upper() == 'K':
    converted = weight1 / 0.45
    print(f'you are {converted} pounds')
elif unit1.upper() == 'L':
    converted = weight1 * 0.45
    print(f'you are {converted} kilos')
