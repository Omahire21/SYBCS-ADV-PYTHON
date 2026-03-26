##SLIP - 18
##Q.1
import os

items = os.listdir()

print("Files and Folders in current directory:")

for i in items:
    print(i)

##Q.2
import re

mobile = input("Enter mobile number: ")

pattern = r"^(0|91)?[6-9][0-9]{9}$"

if re.match(pattern, mobile):
    print("Valid Mobile Number")
else:
    print("Invalid Mobile Number")

##Q.2 - B
def science_subjects():
    return ["Physics","Chemistry","Biology"]

def arts_subjects():
    return ["History","Geography","Political Science"]

print("Science Subjects:")
for s in science_subjects():
    print(s)

print("\nArts Subjects:")
for a in arts_subjects():
    print(a)