# Defining functions
def add(arg1, arg2):
    total = arg1 + arg2
    return total

print(add(3, 5))
print(add(30, 52))



def sum(arg):
    x = 1
    for i in arg:
        x *= i
    return x

out = sum([10,20,30])
print(out)


# Default argument
def greetings(msg="morning"): # default argument
    print(f"Good {msg}")
greetings("evening")


def default_fn(string, integer):
    print(f"Default {string} is having {integer} % efficacy.")
    if integer > 50 and integer < 75:
        print("Seems not so effective, needs more trial.")
    elif integer > 75 and integer < 90:
        print("Can consider this")
    elif integer >= 90:
        print("Sure will take a shot")
    else:
        print("Needs more trials")

default_fn("Unknown", 100)


# *args - It is a tuple
def order_food(min_order, *args):
    print(f"You have ordered: {min_order}")
    for item in args:
        print(f"You have ordered: {item}")
    print("Your food will be delivered in 30 minutes")
    print("Enjoy the party.")

order_food("Salad", "Chicken roll")


# *kwargs - It is a dictionary
import random
def time_activity(*args, **kwargs):
    args_sum = sum(args)
    random_number = random.randint(0, 60)
    min = args_sum + random_number
    choice = random.choice(list(kwargs.keys()))

    print(f"You will have to give {min} mins for your {kwargs[choice]}")


time_activity(10,20,30, hobby="gym", sport="football", fun="chill", work="Software Engineer")