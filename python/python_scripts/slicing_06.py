planet1 = 'Closest to the Sun'
print(planet1)

# print(planet1[4])
# print(planet1[3])

# print(planet1[-3])
# print(planet1[-1])

# Slicing a string, get a substring from a string
print(planet1[1:4])
print(planet1[:7])
print(planet1[15:])


# Slicing tuples
devops = ("Linux", "Vagrant", "Bash Scripting", "AWS", "Jenkins", "Python")
print(devops[2])
print(devops[2:4])
print(devops[2:5][0])
print(devops[2:5][0][5:11])


# Slicing lists
devops01 = ("Linux", "Vagrant", "Bash Scripting", "AWS", "Jenkins", "Python")
print(devops01[2])
print(devops01[2:4])
print(devops01[2:5][0])
print(devops01[2:5][0][5:11])


# Dictionary examples
skills = {"devOps" : ("Linux", "Vagrant", "Bash Scripting", "AWS", "Jenkins", "Python"), "development" : ["Java", "Node", "Javascript"]}

print(skills["devOps"])
print(skills["development"][1:][0][:2])