##SLIP - 13
## Q.1
import time

# current time in seconds
current = time.time()

print("Current time in seconds:", current)

# convert seconds to readable string
print("Readable time:", time.ctime(current))

# convert seconds to struct_time in UTC
print("UTC struct_time:", time.gmtime(current))

##Q.2
filename = input("Enter file name: ")

try:
    f = open(filename, "r")

    print("File contents with pointer position:")

    while True:
        line = f.readline()
        if not line:
            break

        print(line.strip())
        print("Pointer position:", f.tell())

    # move pointer to beginning
    f.seek(0)

    print("\nFile content again:")
    print(f.read())

    f.close()

except FileNotFoundError:
    print("File does not exist")

## Q.2 - B
import pandas as pd

# Student 1
student1 = pd.DataFrame({
    "ID": ["S1","S2","S3","S4","S5"],
    "Name": ["Anita","Sakshi","Om","Raj","Kanika"],
    "Age": [18,23,20,21,20]
})

# Student 2
student2 = pd.DataFrame({
    "ID": ["S2","S4","S5","S6","S7"],
    "City": ["Pune","Nashik","Mumbai","Delhi","Nanded"],
    "Marks": [97,78,86,66,54]
})

print("Student 1")
print(student1)

print("\nStudent 2")
print(student2)

# join dataframes
student3 = pd.merge(student1, student2, on="ID")

print("\nJoined DataFrame")
print(student3)