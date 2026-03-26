##SLIP - 29
##Q.1
import pandas as pd

# read csv file
df = pd.read_csv("Iris.csv")

print("DataFrame Contents:")
print(df)

print("\nStatistical Information:")
print(df.describe())

##Q.2
filename = input("Enter file name: ")
text = input("Enter string to append: ")

try:
    f = open(filename, "a")
    f.write("\n" + text)
    f.close()

    f = open(filename, "r")
    print("File Content:")
    print(f.read())
    f.close()

except FileNotFoundError:
    print("File does not exist")

##Q.2 - B
import re

mobile = input("Enter mobile number: ")

pattern = r"^(0|91)?[6-9][0-9]{9}$"

if re.match(pattern, mobile):
    print("Valid Mobile Number")
else:
    print("Invalid Mobile Number")
    