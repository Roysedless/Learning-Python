# Logical Operators Lesson (8)
# ^^ we use Logical Operators in situations where we have multiples conditions.
# ^ AND Logical Operators. (all the Logical Operators need to be true)
# >> exercise for the example:
#       >  if applicant has high income AND good credit,
#              Eligible for loan.
has_high_income = True
has_good_credit = True

if has_high_income and has_good_credit:
    print("Eligible for loan")

# OR Logical Operators. (must one of the Logical Operators need to be true)
# >> exercise for the example:
#       >  if applicant has high income OR good credit,
#              Eligible for loan.
has_high_income1 = False
has_good_credit1 = True

if has_high_income1 or has_good_credit1:
    print("Eligible for loan")

# NOT Logical Operators (it's inverses any boolean value we give it)
# >> adding:
#     > if applicant has good credit and doesn't have a criminal record.
has_good_credit2= True
has_criminal_record = False

if has_good_credit2 and not has_criminal_record:
    print("Eligible for loan")
