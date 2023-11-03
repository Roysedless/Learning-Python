# String Function (5)
# String Character (Function)
# ^^ is a way to make defined word (character) on a string.
course_character = 'python for beginners'
print(course_character[0])  # using square brackets to get a character that give us an index in the string.
print(course_character[-1])  # example: to use a negative value of a character.
print(course_character[0:3])  # example: sum of range of character.
print(course_character[0:])  # example: if you don't put an end value, python automatic select the maximum value.
print(course_character[:6])  # example: if you don't put an start value, python automatic select the minimum value.
# Formatted String (Function)
# ^^ is a way to mixed string in a complex manner in different a context.
first = 'John'
last = 'Smith'
massage = first + ' [' + last + '] is a coder'  # the hard way and not ideal [string concatenation].
print(f'{first} [{last}] is a coder')  # the easier and understand way [string formatted]. (with a use of curly braces)
# ^ Len Function (general function)
# len function is a way count the number of word (character) on a string, and list bun we learn that later
course = 'Python for Beginners'
print(len(course))  # we use a 'len' function in the parenthesis.

# String Methods
# ^^ is a way to
# ^ Dot Operator using a dot on a string specific methods to a string.
course1 = 'Python for Beginners'
print(course1.upper())  # create a new string that his word is in uppercase.
print(course1.lower())  # create a new string that his word is in lowercase.
# *Not wrong with using an uppercase or lowercase*
print(course1.find('P'))  # show the index of the occurrence by the word (character) that we select.
print(course1.find('Beginners'))  # that show us the occurrence of the first number string that selected 'B'.
print(course1.replace('Beginners', 'Absolute Beginners'))  # we add a comma to use a replace methods.
print(course1.replace('P', 'j'))  # we can use a replace methode in just a one Letter.
print(course1.title())  # it makes a first letter of all first word in uppercase like a title.
print(course1)  # important to emphasize that the original string stay the same.
# The In Operator
print('python' in course1)  # an expression that check if the string contains the word 'python' for example,
# that produces a boolean value.


