##SLIP - 30
##Q.1
s = input("Enter string: ")

# replace a with *
s = s.replace("a","*")

print("Modified string:", s)

##Q.2
def check_pass_fail(marks):
    if marks >= 40:
        return "Pass"
    else:
        return "Fail"


n = int(input("Enter number of students: "))

pass_count = 0
fail_count = 0

for i in range(n):
    m = int(input("Enter marks: "))
    result = check_pass_fail(m)

    print("Result:", result)

    if result == "Pass":
        pass_count += 1
    else:
        fail_count += 1

print("Total Passed:", pass_count)
print("Total Failed:", fail_count)

##Q.2 - B
import time
from datetime import datetime

# a) local and UTC time
print("Local Time:", time.localtime())
print("UTC Time:", time.gmtime())

# b) ctime and gmtime
print("Current time using ctime():", time.ctime())
print("UTC using gmtime():", time.gmtime())

# c) accept date-time
dt = input("Enter date-time (DD-MM-YYYY HH:MM:SS): ")

# d) parse and format
parsed = datetime.strptime(dt,"%d-%m-%Y %H:%M:%S")

print("Format 1:", parsed.strftime("%d/%m/%Y %H:%M"))
print("Format 2:", parsed.strftime("%A, %B %d %Y"))