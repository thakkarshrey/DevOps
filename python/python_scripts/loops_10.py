# For loop

PLANET = "Earth"
for value in PLANET:
    print(f"Value of i is {value}")


NAMES = ("John", "Megan", "Dwayne")
for name in NAMES:
    print(f"My name is {name}")


# While loop
x = 1
while x <=10:
    print(f"Looping.... {x}")
    x+=1


# Nested for loops
NAMES = ("John", "Megan", "Dwayne")

for i in NAMES:
    print(f"My name is {i}")
    for j in i:
        print("##########################")
        print(f"character : {j}")
        print("##########################")




# while loop example
import time
x = 2
while True:
    print(f"Value of x is {x}")
    print("Looping")
    x *= 2
    time.sleep(1)