# F Shape
# ^ Drawing F shape on the terminal
# ^^ with using a Nested Loops

# >> ron solution
# numbers = [5, 2, 5, 2, 2]
#
# for number in numbers:
#     print(number * "x")
# print()
#
# for number in numbers:
#     for index in range(number):
#         print('x', end="")
#     print()
#
# for index, value in enumerate(numbers):
#     print(index, value)

# >> mosh solution
numbers = [5, 2, 5, 2, 2]
total = 0
for x_count in numbers:
    output = ''
    total += x_count
    for count in range(x_count):
        output += 'x'
    print(output)
# modify the values of F Shape
print(total)
