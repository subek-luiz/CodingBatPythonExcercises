"""
Hello Me. This is a code jamming session.
I will be working on several simple pythons codes to be familiar with basics of python language.
My goal is to be a fast,effective programmer who knows the nuts and bolts of python, and it's syntax.
I am using pycharm for this purpose.
"""


# Day 1 : Here we go .................................


# Use Case 1:
# Defining a function
# Using if statement
def a_bigger(a, b):
    if a > b and (a - b) >= 2:
        return True
    else:
        return False


def a_bigger2(a, b):
    if a > b and a - b >= 2:
        return True
    return False


# Calling a function and printing the result
c = a_bigger2(4, 6)
print(c)


# Use Case 2:
# with_no() example function takes in a string and returns a new string with "No:" added at the front
def with_no(str2):
    return "No:" + str2


d = with_no("Subek")
print(d)


# two_e() example method returns True if the string contains exactly two 'e' chars
def two_e(str1):
    count = 0
    for ch in str1:
        if ch == "e":
            count += 1
    if count == 2:
        return True
    return False


print(two_e("Subek"))
