##📄 Slip 2
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

#Q2 – IPL DataFrame
import pandas as pd
import numpy as np

data = {
    "Player": ["Hardik Pandya","K L Rahul","Andre Russel","Jasprit Bumrah","Virat Kohli","Rohit Sharma"],
    "Team": ["Mumbai Indians","Kings Eleven","Kolkata Knight Riders","Mumbai Indians","RCB","Mumbai Indians"],
    "Category": ["Batsman","Batsman","Batsman","Bowler","Batsman","Batsman"],
    "BidPrice": [13,12,None,10,17,None],
    "Runs": [1000,2400,900,200,3600,3700]
}

df = pd.DataFrame(data)

print("DataFrame:\n",df)

# a) first 2 rows
print(df.head(2))

# b) last 3 rows
print(df.tail(3))

# c) check null values
print(df.isnull())

# d) replace null with mean
df["BidPrice"].fillna(df["BidPrice"].mean(), inplace=True)
print(df)

# e) most expensive player
print(df.loc[df["BidPrice"].idxmax()])

# f) players per team
print(df["Team"].value_counts())

#Q.2 - B
class MarksException(Exception):
    pass

try:
    marks = int(input("Enter marks: "))

    if marks < 0 or marks > 100:
        raise MarksException("Marks should be between 0 and 100")

    if marks >= 75:
        grade = "A"
    elif marks >= 60:
        grade = "B"
    elif marks >= 50:
        grade = "C"
    else:
        grade = "Fail"

    print("Grade:", grade)

except ValueError:
    print("Invalid input! Please enter numeric value.")

except MarksException as e:
    print(e)