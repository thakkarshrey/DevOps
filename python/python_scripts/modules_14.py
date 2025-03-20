import random
def order_food(min_order, *args):
    print(f"You have ordered: {min_order}")
    for item in args:
        print(f"You have ordered: {item}")
    print("Your food will be delivered in 30 minutes")
    print("Enjoy the party.")


def time_activity(*args, **kwargs):
    args_sum = sum(args)
    random_number = random.randint(0, 60)
    min = args_sum + random_number
    choice = random.choice(list(kwargs.keys()))

    print(f"You will have to give {min} mins for your {kwargs[choice]}")


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