# Day 3 starts here

# Python string syntax and use-cases
s = "hello"
length = len(s)

print(length)
print(s[0])
print(s[4])
print(s[length-1])

# Add string - Use a symbol '+' for this purpose

t = s+' hi!'
print(t)

# String Slicing - Syntax s[i:j] - These numbers are exclusive
# hello
# 01234
print(s[1:4])
print(s[1:2])
print(s[1:3])
print(s[2:4])
print(s[2:3])

a = 'Hi!'
b = 'Hello'

# Compute c as the first 2 char of a followed by the last 2 char of b
c = a[:2] + b[len(b)-2:]
print(c)

# Negative index - '-1' -> last character / '-2' -> next to the last character
# Hello
# -5-4-3-2-1
print(s[-3:])
print(s[-1:])
print(s[:-1])
print(s[-4:-2])
print(s[-5:5])
print(s[0:5])

# Python String loops
# Range syntax : range(n) -> range(5)=[0,1,2,3,4]/range(5)=[0,5]

s = "Hello"
print(range(len(s)))

for i in range(len(s)):
    print(i)

result = ""
for i in range(len(s)):
    result = result+s[i]
print(result)

result1 = ""
for ch in s:
    result1 = result1+ch
print(result1)

result2 = ""
for ch2 in s:
    result2 = result2+ch2
print(result2)





