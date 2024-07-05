# Day 5 starts here

# Given two int values, return their sum. Unless the two values are the same, then return double their sum.

def sum_double(a, b):
    sum = a + b
    if a == b:
        sum = sum * 2
    return sum


# Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n
# is over 21.

def diff21(n):
    if n > 21:
        return 2 * (n - 21)
    return 21 - n


# We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. We are in trouble
# if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.

def parrot_trouble(talking, hour):
    if talking and (hour < 7 or hour > 20):
        return talking
    return False


# Given 2 ints, a and b, return True if one of them is 10 or if their sum is 10.

def makes10(a, b):
    if a == 10 or b == 10 or a + b == 10:
        return True
    return False


# Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.

def near_hundred(n):
    return (abs(100 - n) <= 10) or (abs(200 - n) <= 10)


# Given 2 int values, return True if one is negative and one is positive. Except if the parameter "negative" is True,
# then return True only if both are negative.

def pos_neg(a, b, negative):
    if negative:
        return a < 0 and b < 0
    else:
        return (a < 0 and b > 0) or (a > 0 and b < 0)


# Given a string, return a new string where "not " has been added to the front. However, if the string already begins
# with "not", return the string unchanged.

def not_string(str):
    if len(str) >= 3 and str[:3] == 'not':
        return str
    else:
        return 'not ' + str


# Given a non-empty string and an int n, return a new string where the char at index n has been removed. The value of
# n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).

def missing_char(str, n):
    front = str[:n]
    back = str[n + 1:]
    return front + back


# Given a string, return a new string where the first and last chars have been exchanged.

def front_back(str):
    if len(str) <= 1:
        return str
    else:
        return str[-1] + str[1:-1] + str[0]


# Given a string, we'll say that the front is the first 3 chars of the string. If the string length is less than 3,
# the front is whatever is there. Return a new string which is 3 copies of the front.

def front3(str):
    return str[0:3] + str[0:3] + str[0:3]


# ------------------------ Warmup - 1 ends here -----------------------------------------------
"""
Given a string and a non-negative int n, return a larger string that is n copies of the original string.
string_times('Hi', 2) → 'HiHi'
string_times('Hi', 3) → 'HiHiHi'
string_times('Hi', 1) → 'Hi'
"""


def string_times(str, n):
    str1 = ''
    for i in range(n):
        str1 += str
    return str1



