DevOps = ["Javascript", "Jenkins", "Bash", "Python", "Ansible", "Docker", "Kubernetes"]
Development = ("React", "Javascript", "Html", "CSS", "NodeJs", "Postgres")
emp_01 = {
    "name" : "John Doe",
    "code" : 1024,
    "skill" : "Backend"
}

emp_02 = {
    "name" : "",
    "code" : 1021,
    "skill" : "Frontend"
}
 
user_skill = input("Enter your desired skill: ")
# print(user_skill)

if user_skill in DevOps:
    print(f"We have {user_skill} skill in DevOps team")
elif user_skill in Development:
    print(f"We have {user_skill} skill in Development team")
elif user_skill in emp_01.values() or user_skill in emp_02.values():
    print(f"We have employess with {user_skill} skill")
else:
    print("No skill found!")
