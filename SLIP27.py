##SLIP - 27
##Q.1
import random
import math

# generate random radius
r = random.randint(1,10)

# circumference formula
circumference = 2 * 3.14 * r

print("Radius:", r)
print("Circumference:", circumference)

##Q.2
import re

password = input("Enter password: ")

pattern = r"^(?=.*[a-z])(?=.*[0-9])(?=.*[$#@]).{6,12}$"

if re.match(pattern, password):
    print("Valid Password")
else:
    print("Invalid Password")

##Q.2 - B
import os

files = os.listdir()

count = 0

for f in files:
    print(f)
    
    if f.endswith(".py"):
        count += 1

print("Total .py files:", count)

for f in files:
    if f.endswith(".py"):
        file = open(f,"r")
        print("\nContent of",f)
        print(file.read())
        file.close()
        break