# Day 4 starts here

# Create a list
a = ['hi', 'there', '1']
print(len(a))
print(a[0])
print(a[1])
print(a[2])
a[2] = 'ho'
print(a[2])

# append(value) method and sorted(list) method
a = ['hi', 'there']
a.append('aa')
a.append('bb')
print(a)
b = sorted(a)
print(b)

# Python List Loop
a = [1, 2, 3]
total = 0
for num in a:
    total += num
print(total)

# Another way to loop a list
a = ['hi', 'there', 'ok']
result = ''
for i in range(len(a)):
    result += a[i] + ' '
print(result)

# Python If Boolean logic - ==, !=, <, <=, >, >=
a = 'Hello'


def if_demo(s):
    if s == 'Hello' or s == 'Hi':
        s = s + ' nice to meet you'
    else:
        s = s + ' woo hoo!'
    return s


print(if_demo(a))


# --------------------------------- End of Revision ------------------------------------------

# --------------------------------- Warmup-1 -------------------------------------------------

# sleep_in
# The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation.
# We sleep in if it is not a weekday, or we're on vacation. Return True if we sleep in.

def sleep_in(weekday, vacation):
    if not weekday or vacation:
        return True
    else:
        return False


print(sleep_in(True, False))


def sleep_in(weekday, vacation):
    return not weekday or vacation


# monkey_trouble
# We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. We
# are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.

def monkey_trouble(a_smile, b_smile):
    return (a_smile and b_smile) or (not a_smile and not b_smile)





