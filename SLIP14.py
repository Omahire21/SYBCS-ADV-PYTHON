##SLIP - 14
##Q.1
import re

s = input("Enter string: ")
sub = input("Enter substring: ")

pattern = "^" + sub   # check at beginning

if re.match(pattern, s):
    print("Substring is present at the beginning.")
else:
    print("Substring is NOT present at the beginning.")

##Q.2
filename = input("Enter file name: ")
pos = int(input("Enter byte position: "))

try:
    f = open(filename, "r")

    f.seek(pos)   # move pointer

    print("Content from given position:")
    print(f.read())

    f.close()

except FileNotFoundError:
    print("File does not exist")

##Q.2 - B
# factorial function
def factorial(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f

# power dictionary
power = {2:4, 3:9, 4:16, 5:25}

# vowels list
vowels = ['a','e','i','o','u']

n = int(input("Enter number: "))

print("Factorial:", factorial(n))
print("Power:", power.get(n, "Not available"))
print("Second vowel:", vowels[1])