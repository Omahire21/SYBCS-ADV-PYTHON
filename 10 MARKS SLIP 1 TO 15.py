#SLIP - 1
#Q1. Write Python code to create a dictionary containing mobile names and their prices.Create DataFrame from this dictionary. Display the contents of DataFrame.#

import pandas as pd

# Creating dictionary
data = {
    "Mobile_Name": ["Samsung", "Redmi", "Realme", "iPhone"],
    "Price": [20000, 15000, 18000, 70000]
}

# Creating DataFrame
df = pd.DataFrame(data)

# Display DataFrame
print("Mobile DataFrame:")
print(df)
-------------------------------------------------------------------------------------------------
## SLIP - 2
##Q1 – Vowels, Consonants, Special Symbols (10 MARKS)
s = input("Enter a string: ")

vowels = 0
consonants = 0
special = 0

for ch in s:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1
    else:
        special += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Special Symbols:", special)
-------------------------------------------------------------------------------------------------
#SLIP - 3
#Q.1
try:
    m = int(input("Enter value of m: "))
    n = int(input("Enter value of n: "))

    result = m / n
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
-------------------------------------------------------------------------------------------------
##SLIP - 4
#Q.1
import random

# create list
lst = [10, 20, 30, 40, 50]

print("Original List:", lst)

# shuffle list
random.shuffle(lst)

print("Shuffled List:", lst)
-------------------------------------------------------------------------------------------------
##SLIP - 5
#Q.1
s = input("Enter a string: ")

words = s.split()

print("Words without vowels:")

for w in words:
    if not any(v in w.lower() for v in "aeiou"):
        print(w)
-------------------------------------------------------------------------------------------------
# SLIP - 6
# Q.1
try:
    a = input("Enter first number: ")
    b = input("Enter second number: ")

    if not a.isnumeric() or not b.isnumeric():
        raise TypeError("Input must be numeric")

    a = int(a)
    b = int(b)

    print("Sum:", a + b)

except TypeError as e:
    print(e)
-------------------------------------------------------------------------------------------------
#SLIP - 7
#Q.1
import re

s = input("Enter a string: ")

# remove special characters
clean = re.sub(r'[^A-Za-z\s]', '', s)

# extract words starting with capital letter
words = clean.split()

print("Words starting with capital letter:")
for w in words:
    if w[0].isupper():
        print(w)

print("Modified String:", clean)
-------------------------------------------------------------------------------------------------
## SLIP -8
## Q.1
def area(radius):
    return 3.14 * radius * radius

r = float(input("Enter radius: "))

result = area(r)

print("Area of Circle:", result)
-------------------------------------------------------------------------------------------------
## SLIP 9
## Q.1
def even_generator(n):
    for i in range(2, n+1, 2):
        yield i

n = int(input("Enter value of n: "))

print("Even numbers up to", n)

for num in even_generator(n):
    print(num)
-------------------------------------------------------------------------------------------------
## SLIP - 10
## Q.1
import pandas as pd

# list of 10 integers
data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

df = pd.DataFrame(data, columns=["Numbers"])

print("DataFrame:")
print(df)

print("Sum:", df["Numbers"].sum())
print("Mean:", df["Numbers"].mean())
print("Median:", df["Numbers"].median())
print("Mode:", df["Numbers"].mode()[0])
print("Standard Deviation:", df["Numbers"].std())
-------------------------------------------------------------------------------------------------
#SLIP - 11
##Q.1
# create list
lst = [1,2,3,4,5,6,7,8,9,10]

# lambda with map
squares = list(map(lambda x: x*x, lst))

print("Original List:", lst)
print("Squares:", squares)
-------------------------------------------------------------------------------------------------
## SLIP - 12
## Q.1
## MAKE CSV FILE FIRST
##EX.
Name,Designation,Salary
Rahul,Manager,50000
Amit,Developer,40000
Neha,Analyst,45000
Riya,HR,35000

##Q.1
import pandas as pd

df = pd.read_csv("data.csv")

print("DataFrame:")
print(df)

print("\nStatistical Information:")
print(df.describe())
-------------------------------------------------------------------------------------------------
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
-------------------------------------------------------------------------------------------------
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
-------------------------------------------------------------------------------------------------
## SLIP - 15
## Q.1
import time

# current time in seconds
t = time.time()

# a) convert seconds to struct_time in UTC
utc_time = time.gmtime(t)
print("UTC struct_time:", utc_time)

# b) convert struct_time to formatted string
formatted = time.strftime("%d-%m-%Y %H:%M:%S", utc_time)
print("Formatted Time:", formatted)