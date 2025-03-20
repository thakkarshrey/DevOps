message = "random message"
Message = message.capitalize()
print(Message)

# dir function
print(dir(""))
print(dir([]))
print(dir({}))


print(message.upper())
print(message.islower()) # True
print(message.isupper()) # False

print(message.find("mess"))

print(message[7:11])


seq01 = ('192', '168','40','90')
print(".".join(seq01))
print("/".join(seq01))


mountains = ["Everest", "Himalaya", "Sayadri"]
mountains.append('Oregon mount')

print(mountains)

mountains.extend(["Mt Rainer", "Satpuda"])
print(mountains)

mountains.insert(2, 'Mt Abu')
print(mountains)

mountains.pop()
mountains.pop()
print(mountains)

mountains.pop(2)
print(mountains)


emp_01 = {
    "name" : "Dwane Johnson",
    "skill" : "Actor",
    "code" : 1024
}
print(emp_01.keys())
print(emp_01.values())

emp_01.clear()
print(emp_01)