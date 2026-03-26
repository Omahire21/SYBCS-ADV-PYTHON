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

## Q.2
import time
from datetime import datetime

# current local time
print("Local Time:", time.ctime())

# UTC time
print("UTC Time:", time.gmtime())

# accept date-time
dt = input("Enter date-time (DD-MM-YYYY HH:MM:SS): ")

# parse string
parsed = datetime.strptime(dt, "%d-%m-%Y %H:%M:%S")

# format in two ways
print("Format 1:", parsed.strftime("%d/%m/%Y %H:%M"))
print("Format 2:", parsed.strftime("%A, %B %d %Y"))

##Q.2 - B
import random

lst = [10,20,30,40,50]
s = "PYTHON"
t = (1,2,3,4,5)

print("Random from list:", random.sample(lst,3))
print("Random from string:", random.sample(s,3))
print("Random from tuple:", random.sample(t,3))