# Variables Learning (2)
# ^^ Variables is an option, to store data in a computer memory.
# ^ to use variables, we attach the name of the variable, to his value (str), (int)....
price = 10  # variable(int).
rating = 4.9  # variable(float).
name = 'roy sadless'  # variable(str).
is_published = False  # variable(bool).
# you can add different class of data
birth_year = 2000 + int('my birth day')
price_ = "good price" + str(50)

# print add option with a variables
# ^ you can print a variable. the value of the variable copy (str, int, float).
print(name)  # variable print
print(name + " can do it")  # variable + the same value of a variable (str)
print(price + 5)  # variable + the same value of a variable (int)
print(rating + 6.5)  # variable + the same value of a variable (float)
print(f"{name} {rating}")  # variable + different value variable [string formatted]
print(name + " " + str(price))  # variable + different value variable [string concatenation]
print(f"{name} {is_published} good day {10}")  # variable + str/int + different [string formatted]
print(name + " " + str(price) + " good day" + " " + str(10))  # variable + str/int + different [string concatenation]
