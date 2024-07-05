# Day 2 is here

# Python List

# 1. pair_13() example function returns True if the list(num) contains a pair of 13's next to each other.


def pair_13(num):
    for i in range(len(num) - 1):
        if num[i] == 13 and num[i + 1] == 13:
            return True
            # a = 5
    return False


list1 = [12, 12, 13, 13, 15, 17, 18]

print(pair_13(list1))
