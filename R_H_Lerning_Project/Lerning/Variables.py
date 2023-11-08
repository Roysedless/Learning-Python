# Variables Lesson (2)
# ^^ Variables is an option, to store data in a computer memory.
# ^ To use variables, we attach the name of the variable, to his value (str,int,float) >>
price = 10  # variable = integer.
rating = 4.9  # variable = float.
name = 'roy con'  # variable = string.
is_published = False  # variable = boolean.
# you can set a variables in different mixed (str,int,float) >>
birth_year = 2000 + int('my birth day')
price_ = "good price" + str(50)

# You can print a variables and print variables in different mixed (str,int,float) >>
# ^ The value of the variable equal to the set value hs been defined (str,int,float).
print(name)  # variable print
print(name + " can do it")  # (variable = str) + string
print(price + 5)  # (variable = int) + integer
print(rating + 6.5)  # (variable = float) + float
print(f"{name} {rating}")  # variable + different value variable [string formatted]
print(name + " " + str(price))  # variable + different value variable [string concatenation]
print(f"{name} {is_published} good day {10}")
# ^ variable + variables different value + (str,int,float) [string formatted]
print(name + " " + str(price) + " good day" + " " + str(10))
# ^ variable + variables different value + (str,int,float) [string concatenation]
