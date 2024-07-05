# Day 8 starts here
""""""
"""
You and your date are trying to get a table at a restaurant. The parameter "you" is the stylishness of your clothes,
in the range 0..10, and "date" is the stylishness of your date's clothes. The result getting the table is encoded as 
an int value with 0=no, 1=maybe, 2=yes. If either of you is very stylish, 8 or more, then the result is 2 (yes). 
With the exception that if either of you has style of 2 or less, then the result is 0 (no). Otherwise the result is 1 (maybe).

date_fashion(5, 10) → 2
date_fashion(5, 2) → 0
date_fashion(5, 5) → 1
"""


def date_fashion(you, date):
    if you <= 2 or date <= 2:
        return 0
    if you >= 8 or date >= 8:
        return 2
    else:
        return 1


"""
You are driving a little too fast, and a police officer stops you. Write code to compute the result, 
encoded as an int value: 0=no ticket, 1=small ticket, 2=big ticket. If speed is 60 or less, the result is 0. If speed is between 61 and 80 inclusive, the result is 1. If speed is 81 or more, the result is 2. Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.

caught_speeding(60, False) → 0
caught_speeding(65, False) → 1
caught_speeding(65, True) → 0
"""


def caught_speeding(speed, is_birthday):
    if is_birthday:
        bonus = 5
    else:
        bonus = 0
    if speed <= 60 + bonus:
        return 0
    elif 61 + bonus <= speed <= 80 + bonus:
        return 1
    elif speed >= 81 + bonus:
        return 2


"""
Given 2 ints, a and b, return their sum. However, sums in the range 10..19 inclusive, are forbidden, so in that case just return 20.

sorta_sum(3, 4) → 7
sorta_sum(9, 4) → 20
sorta_sum(10, 11) → 21
"""


def sorta_sum(a, b):
    if 10 <= a + b <= 20:
        return 20
    else:
        return a + b


"""
Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a boolean indicating if we are on vacation, 
return a string of the form "7:00" indicating when the alarm clock should ring. Weekdays, the alarm should be "7:00" 
and on the weekend it should be "10:00". Unless we are on vacation -- then on weekdays it should be "10:00" and weekends it should be "off".

alarm_clock(1, False) → '7:00'
alarm_clock(5, False) → '7:00'
alarm_clock(0, False) → '10:00'
"""


def alarm_clock(day, vacation):
    if vacation:
        if day == 0 or day == 6:
            return 'off'
        else:
            return '10:00'
    else:
        if day == 0 or day == 6:
            return '10:00'
        else:
            return '7:00'


"""
The number 6 is a truly great number. Given two int values, a and b, return True if either one is 6. 
Or if their sum or difference is 6. Note: the function abs(num) computes the absolute value of a number.

love6(6, 4) → True
love6(4, 5) → False
love6(1, 5) → True
"""


def love6(a, b):
    return a == 6 or b == 6 or a + b == 6 or abs(a - b) == 6


"""
Given a number n, return True if n is in the range 1..10, inclusive. Unless outside_mode is True, in which case return 
True if the number is less or equal to 1, or greater or equal to 10.

in1to10(5, False) → True
in1to10(11, False) → False
in1to10(11, True) → True
"""


def in1to10(n, outside_mode):
    if outside_mode:
        return n <= 1 or n >= 10
    else:
        return 1 <= n <= 10


"""
Given a non-negative number "num", return True if num is within 2 of a multiple of 10. Note: (a % b) is the remainder of 
dividing a by b, so (7 % 5) is 2. See also: Introduction to Mod

near_ten(12) → True
near_ten(17) → False
near_ten(19) → True
"""


def near_ten(num):
    a = num % 10
    return a <= 2 or a >= 8


# ----------------------------------------- Logic 1 Ends here ------------------------------------


# ----------------------------------------- Logic 2 Starts here ----------------------------------

"""We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big 
bricks (5 inches each). Return True if it is possible to make the goal by choosing from the given bricks. This is a 
little harder than it looks and can be done without any loops. See also: Introduction to MakeBricks 

make_bricks(3, 1, 8) → True
make_bricks(3, 1, 9) → False
make_bricks(3, 2, 10) → True
"""


def make_bricks(small, big, goal):
    # fail 1 not enough bricks
    if small * 1 + big * 5 < goal:
        return False

    # fail 2 not enough small bricks
    if goal % 5 > small:
        return False

    return True


"""
Given 3 int values, a b c, return their sum. 
However, if one of the values is the same as another of the values, it does not count towards the sum.

lone_sum(1, 2, 3) → 6
lone_sum(3, 2, 3) → 2
lone_sum(3, 3, 3) → 0
"""


def lone_sum(a, b, c):
    sum = 0
    if a != b and a != c:
        sum += a
    if b != a and b != c:
        sum += b
    if c != a and c != b:
        sum += c

    return sum


"""
Given 3 int values, a b c, return their sum. However, if one of the values is 13 then it does not count towards
the sum and values to its right do not count. So for example, if b is 13, then both b and c do not count.

lucky_sum(1, 2, 3) → 6
lucky_sum(1, 2, 13) → 3
lucky_sum(1, 13, 3) → 1
"""


def lucky_sum(a, b, c):
    if a == 13:
        return 0
    elif b == 13:
        return a
    elif c == 13:
        return a + b
    else:
        return a + b + c


"""Given 3 int values, a b c, return their sum. However, if any of the values is a teen -- in the range 13..19 
inclusive -- then that value counts as 0, except 15 and 16 do not count as a teens. Write a separate helper 
"def fix_teen(n):"that takes in an int value and returns that value fixed for the teen rule. In this way, 
you avoid repeating the teen code 3 times (i.e. "decomposition"). Define the helper below and at the same indent 
level as the main no_teen_sum(). 

no_teen_sum(1, 2, 3) → 6
no_teen_sum(2, 13, 1) → 3
no_teen_sum(2, 1, 14) → 3
"""


def no_teen_sum(a, b, c):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)


def fix_teen(n):
    if 13 <= n <= 14 or 17 <= n <= 19:
        return 0
    else:
        return n


"""For this problem, we'll round an int value up to the next multiple of 10 if its rightmost digit is 5 or more, 
so 15 rounds up to 20. Alternately, round down to the previous multiple of 10 if its rightmost digit is less than 5, 
so 12 rounds down to 10. Given 3 ints, a b c, return the sum of their rounded values. To avoid code repetition, 
write a separate helper "def round10(num):" and call it 3 times. Write the helper entirely below and at the same 
indent level as round_sum(). 

round_sum(16, 17, 18) → 60
round_sum(12, 13, 14) → 30
round_sum(6, 4, 4) → 10
"""


def round_sum(a, b, c):
    return round10(a) + round10(b) + round10(c)


def round10(num):
    mod = num % 10
    num -= mod
    if mod >= 5:
        num += 10
    return num


"""Given three ints, a b c, return True if one of b or c is "close" (differing from a by at most 1), while the other 
is "far", differing from both other values by 2 or more. Note: abs(num) computes the absolute value of a number. 

close_far(1, 2, 10) → True
close_far(1, 2, 3) → False
close_far(4, 1, 3) → True"""


def close_far(a, b, c):
    return (abs(a - b) <= 1 or abs(a - c) <= 1) and ((abs(a - b) >= 2 or abs(a - c) >= 2) and abs(b - c) >= 2)


"""We want make a package of goal kilos of chocolate. We have small bars (1 kilo each) and big bars (5 kilos each). 
Return the number of small bars to use, assuming we always use big bars before small bars. Return -1 if it can't be 
done. 

make_chocolate(4, 1, 9) → 4
make_chocolate(4, 1, 10) → -1
make_chocolate(4, 1, 7) → 2"""


def make_chocolate(small, big, goal):
    # fail case 1
    if small * 1 + big * 5 < goal:
        return -1
    # fail case 2
    if goal % 5 > small:
        return -1
    # numbers of big and small chocolates
    if goal // 5 >= big:
        return goal - big * 5
    else:
        return goal - goal // 5 * 5


"""Given a string, return a string where for every char in the original, there are two chars.

double_char('The') → 'TThhee'
double_char('AAbb') → 'AAAAbbbb'
double_char('Hi-There') → 'HHii--TThheerree'"""


def double_char(str):
    result = ''
    for i in range(len(str)):
        result += str[i] + str[i]
    return result


"""Return the number of times that the string "hi" appears anywhere in the given string.

count_hi('abc hi ho') → 1
count_hi('ABChi hi') → 2
count_hi('hihi') → 2"""


def count_hi(str):
    count = 0
    for i in range(len(str)):
        if str[i:i + 2] == 'hi':
            count += 1
    return count





