# Arithematic Operators
x = 10
y = 5
total = x + y
print(total)


total = x - y
print(total)


total = x * y
print(total)

total = x/y
print(total)

total = x%y
print(total)

total = x**y
print(total)


# Comparison operators
a = 30
b = 60

out = (a < b)
print(out)

out = (a == b)
print(out)

out = (a != b)
print(out)

out = (a >= b)
print(out)

out = (a <= b)
print(out)


# Assignment operators
c = 0
d = 1

c += d # c = c + d
print(c)


# Logical operators
# and 
# or

a = 40
b = 60

x = 2
y = 3

# or operator
log = (a < b) or (x > y)
print(log)

log = (a > b) or (x < y)
print(log)

log = (a > b) or (x > y)
print(log)

# and operator
log = (a < b) and (x > y)
print(log)

log = (a > b) and (x < y)
print(log)

log = (a < b) and (x < y)
print(log)

# not operator
log = not(x < y)
print(log)





# Membership operator
first_tuple = ("React", "DevOps", 45, 12.4)
ans = "React" in first_tuple
print(ans)

ans = "React" not in first_tuple
print(ans)

ans = 12.4 in first_tuple
print(ans)



# Identity operator
a = 12
b = 34

result = a is b
print(result)

result = a is not b
print(result)