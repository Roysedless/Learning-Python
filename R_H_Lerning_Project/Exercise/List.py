# List (Exercise)
# >> write a program to find the largest numbers in a list
numbers = [1, 4, 9, 10, 3, 5]
max_num = numbers[0]
for curr_num in numbers:
    if curr_num > max_num:
        max_num = curr_num
print(max_num)