# Arithmetic Operation (6)
# ^^ we have a different selection for Arithmetic Operation in python like this >>
print(10 + 3)  # Addition Operation.
print(10 + 3)  # Subtraction Operation.
print(10 * 3)  # Multiplication Operation.
print(10 / 3)  # Standard Division Operation (we can get a float number).
print(10 // 3)  # Other Division Operation (we get an integer number).
print(10 % 3)  # Modulis Operation (this returns the remainder of the division).
print(10 ** 3)  # Exponent Operation (power).

# Augmented Assignment Operation.
# ^ a way to write the same Mathematica Arithmetic but in shorter form >>
x = 10
x += 4  # instead of x = x + 4
x -= 4  # instead of x = x - 4
x *= 2  # instead of x = x * 4
x **= 2  # instead of x = x ** 4
x /= 2  # instead of x = x / 4
x //= 5  # instead of x = x // 4
# Operator Precedence
# ^ it's just a basic math concept of "Operator Precedence".
X1 = 10 * 5 + (5 + 3)  # parenthesis () (First 1)
X2 = 10 / 5 ** 3  # Exponentiation (Second 2).
X3 = 10 + 3 * 10 / 4  # Multiplication, or, Division (Third 3).
X4 = 10 + 4 - 3  # Addition, or, Subtraction (Fourth 4)

#  Math Functions (method)
# ^^ Function with using numbers (int,float)
x = -2.6  # for this example
print(round(x))  # is a build in function to round the number (int > float).
print(abs(x))  # is a build in function to gat allways the positive number.
import math  # > we import a math module, and now math is an object like a string.
# we can access math methods using a dot operator.
print(math.ceil(2.9))  # ceil use to round the number. (like the build in function round ^)
print(math.floor(2.9))  # floor use to round down the number.
# to learn more about the math module >>
#  *search In Google: "pyton 3 math module" > and there we selected the python official website*
