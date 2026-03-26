##SLIP - 16
##Q.1
import re

word = input("Enter word: ")

pattern = r"^[bh]i?t$|^[bh]u?t$|^[bh]a?t$"

if re.match(pattern, word):
    print("Valid three letter word")
else:
    print("Invalid word")
    
##Q.2
import pandas as pd

data = {
"Player":["Hardik Pandya","K L Rahul","Andre Russel","Jasprit Bumrah","Virat Kohli","Rohit Sharma"],
"Team":["Mumbai Indians","Kings Eleven","Kolkata Knight Riders","Mumbai Indians","RCB","Mumbai Indians"],
"Category":["Batsman","Batsman","Batsman","Bowler","Batsman","Batsman"],
"BidPrice":[13,12,7,10,17,15],
"Runs":[1000,2400,900,200,3600,3700]
}

df = pd.DataFrame(data)

print("DataFrame:")
print(df)

# a) first 2 rows
print("\nFirst 2 rows")
print(df.head(2))

# b) last 3 rows
print("\nLast 3 rows")
print(df.tail(3))

# c) add null value
df.loc[2,"BidPrice"] = None
print("\nAfter adding null value")
print(df)

# d) most expensive player
print("\nMost expensive player")
print(df.loc[df["BidPrice"].idxmax()])

# e) players per team
print("\nPlayers per team")
print(df["Team"].value_counts())

##Q.2 - B
def car_models():
    return ["Swift","Baleno","i20"]

def bike_models():
    return ["Pulsar","Apache","R15"]

print("Available Car Models:")
for c in car_models():
    print(c)

print("\nAvailable Bike Models:")
for b in bike_models():
    print(b)