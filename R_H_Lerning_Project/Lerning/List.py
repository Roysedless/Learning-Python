# List (learning)

names = ['John', 'Bob', 'Mosh', 'sarah', 'Mary']  # defined a list on a variables
print(names)  # print exactly like how do we define our list
print(names[0])  # print individual element using an index
# ^^ And: [3], [4], [2]
print(names[-1])  # negative value refers in the opposite direction
# ^^ And: [-2], [-4], [-1]
print(names[2:3])  # we use a colon to select a range of items
# ^^ And: [1:4], [3:5].
print(names[:4])  # we use an empty value to get the start character
print(names[2:])  # we use an empty value to get the end character
# >> important to mention the square brackets make a new string,
#    not changed the old once.
names[0] = 'Roy'  # we can modify the list by changed his first character.
print(names)

