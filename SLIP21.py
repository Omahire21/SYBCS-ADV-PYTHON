## SLIP - 21
## Q.1
import pandas as pd

data = {
"Subject_Name":["Math","Physics","Chemistry","Biology","English","Computer"],
"Marks":[85,78,82,75,80,90]
}

df = pd.DataFrame(data)

print("First 5 rows:")
print(df.head())

print("\nLast 5 rows:")
print(df.tail())

##Q.2
filename = input("Enter file name: ")

try:
    f = open(filename,"r")

    text = f.read()

    print("File Content:")
    print(text)

    print("Characters:", len(text))
    print("Words:", len(text.split()))
    print("Lines:", len(text.split("\n")))

    f.close()

except FileNotFoundError:
    print("File does not exist")

##Q.2 - B
def open_account(name):
    print("Account created successfully for", name)

def apply_loan(amount):
    print("Loan applied successfully for amount:", amount)

name = input("Enter account holder name: ")
amount = int(input("Enter loan amount: "))

open_account(name)
apply_loan(amount)