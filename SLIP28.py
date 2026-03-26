##SLIP - 28
##Q.1

##Q.2
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

##Q.2 - B
import os

path = os.getcwd()

print("Current Directory:", path)

items = os.listdir(path)

for i in items:
    if os.path.isfile(i):
        print(i, "- File")
    else:
        print(i, "- Folder")
        