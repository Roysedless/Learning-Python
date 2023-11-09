# Variable Practice (3.3)
# exercise: ask two questions, person's name and favourite color.
# Then, print a massage like "Mosh likes blue"
name = input('What is your name? ')
favourite_color = input('What is your favourite color? ')
print(name + " likes " + favourite_color)

# practice variable (3.6)
# exercise: making a birth year calculator .
birth_year = input('birth year? ')
print(type(birth_year))  # type : defines the class of the data (str)
age = 2023 - int(birth_year)
print(type(age))  # type defines the class of the data (int)
print(age)

# practice variable (3.9)
# exercise: making a Ibs to Kg calculator.
weight_Ibs = input('Weight (Ibs)? ')
weight_Kg = int(weight_Ibs) * 0.45
print(weight_Kg)
type(weight_Kg)  # type defines the class of the data (float)
