#!/usr/bin/python3

import os

users = ["alpha", "beta", "gamma"]

print("Adding users.........")
print("##################################################################")
print()

# Adding users to the system
for user in users:
    exit_code = os.system(f"id {user}")

    if exit_code != 0:
        print(f"User does not exist. Adding user {user} to the system")
        print("###############################")
        print()
        os.system(f"useradd {user}")
    else:
        print(f"User {user} already exists!")
        print("###############################")
        print()

print()
print("Adding groups..........")
print("##################################################################")
print()


# Adding groups to the system
group = "science"
if os.system("grep science /etc/group") != 0:
    print(f"Group does not exist. Adding group {group} in the system")
    print("###################################")
    print()
    os.system(f"groupadd {group}")
else:
    print(f"Group {group} already exists!")
    print("###################################")
    print()


# Adding all the users to science group
for user in users:
    print(f"Adding user {user} in the science group")
    print("###################################")
    print()
    os.system(f"usermod -G science {user}")


# Creating a directory and giving permissions to the science group
if os.path.isdir("/opt/science_dir"):
    print("Directory already exists!")
    print("###################################")
    print()
else:
    print("Creating a directory")
    print("###################################")
    print()
    os.system("mkdir science_dir")

print("Assigning permission and ownership to the directory.")
print("################################")
os.system("chown :science /opt/science_dir")
os.system("chmod 770 /opt/science_dir")
