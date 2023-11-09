# String Function (5)
# ^ String Character (Function)
# ^^ Is a way to make defined word (character) on a string.
course_character = 'python for beginners'  # for the example >>
print(course_character[0])  # using square brackets to get a character that give us an index in the string.
print(course_character[-1])  # negative value of a character, to get the opposite direction index.
print(course_character[0:3])  # sum of range of character.
print(course_character[0:])  # if you don't put an end value, python automatic select the maximum value.
print(course_character[:6])  # if you don't put an start value, python automatic select the minimum value.
# ^ Formatted String (Function)
# ^^ Is a way to mixed string in a complex manner in different context.
first = 'John'
last = 'Smith'
massage = first + ' [' + last + '] is a coder'  # the hard way and not ideal [string concatenation].
print(f'{first} [{last}] is a coder')  # the easier way and understand way [string formatted].
#  ^^ (with a use of curly braces)
# ^ Len Function (general function)
# len function is a way count the number of word (character) on a string, and list bun we learn that later
course = 'Python for Beginners'
print(len(course))  # we use a 'len' function to count the number of word on a string.

# String Methods (Dot Operator)
# ^^ is a way to specific methods to a string.
# ^ we do that with using a dot.
course1 = 'Python for Beginners'
print(course1.upper())  # create a new string that his words is in uppercase.
print(course1.lower())  # create a new string that his words is in lowercase.
print(course1.title())  # it makes a first letter of all first word in uppercase just like a title.
# make sure to write the correct uppercase or lowercase if needed to specify the searching >>
print(course1.find('P'))  # show the index of the occurrence by the word (character) that we select.
print(course1.find('Beginners'))  # it's show us the occurrence of the first word string is selected like 'B'.
print(course1.replace('Beginners', 'Absolute Beginners'))  # we add a comma to use a replace methods >>
# replace is a methode to add a replacement word to the word that we selected.
print(course1.replace('P', 'j'))  # we can use a replacement methode with just a one Letter.
print(course1)  # important to emphasize that the original string stay the same.
# The In Operator
print('python' in course1)  # an expression that check if the string contains the word 'python' for example.
# good to know that produces a boolean value.


