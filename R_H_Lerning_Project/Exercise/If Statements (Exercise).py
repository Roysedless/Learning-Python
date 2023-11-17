# If Statements Practice (7)
# exercise: of If Statements >>
# ^^ price of a house is 1M.
#       if buyer has good credit,
#          they need to put down 10%
#       otherwise
#          they need to put down 20%
#    print the down payment
# My solution >>
# my_house_price = 1000000
# my_buyer_good_credit = True
# if my_buyer_good_credit:
#     my_house_price = 0.1 * 1000000
# if not my_buyer_good_credit:
#     my_house_price = 0.2 * 1000000
# print(my_house_price)

# Dana Yaniv solution >>
# dana_house_price = 1000000 * (10 / 100)
# dana_buyer_good_credit = False
# if not dana_buyer_good_credit:
#     dana_house_price = 1000000 * (20 / 100)
# print(dana_house_price)

# Mosh solution >>
lecture_price = 1000000
lecture_has_good_credit = True

if lecture_has_good_credit:
    lecture_down_payment = 0.1 * lecture_price
else:
    lecture_down_payment = 0.2 * lecture_price
print(f'down payment: ${lecture_down_payment}')

# *I make mathematical question with using an if statements*
solution = int(input('What is 5 + 5? '))
if solution == 10:
    print('You Right')
elif 10 > solution > 7 or 13 > solution > 10:
    print('You Wrong')
else:
    print('You So Wrong')
