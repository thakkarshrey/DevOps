# Break
x = "devOps"
for i in x:
    print(f"Value is {i}")
    if i == "O":
        print("Found my data")
        break


# Continue
arr = []
for i in x:
    if i == "O":
        print("Found my data")
        continue
    print(f"Value is {i}")
    arr.append(i)

print(arr)



import random
NAMES = ["John", "Megan", "Dwayne", "Brock", "Usos", "Shrey"]
random.shuffle(NAMES)
LUCKY = random.choice(NAMES)

for i in NAMES:
    if i == LUCKY:
        print("###########################")
        print(f"{i} is the lucky winner")
        print("###########################")
        print()
        break

    print(f"{i} lost. Better luck next time")