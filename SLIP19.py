##SLIP - 19
##Q.1
import random

# deck of cards
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]

deck = []

for s in suits:
    for r in ranks:
        deck.append(r + " of " + s)

# shuffle deck
random.shuffle(deck)

print("Cards obtained by user in 5 attempts:")

for i in range(5):
    print(deck[i])

##Q.2
import os

path = os.getcwd()

print("Current Directory:", path)

items = os.listdir(path)

for item in items:
    if os.path.isfile(item):
        print(item, "- File")
    else:
        print(item, "- Folder")

##Q.2 - B
import pandas as pd

data = {
"Player":["Hardik Pandya","K L Rahul","Andre Russel","Jasprit Bumrah","Virat Kohli","Rohit Sharma"],
"Team":["Mumbai Indians","Kings Eleven","Kolkata Knight Riders","Mumbai Indians","RCB","Mumbai Indians"],
"Category":["Batsman","Batsman","Batsman","Bowler","Batsman","Batsman"],
"BidPrice":[None,12,7,10,None,15],
"Runs":[1000,2400,900,200,3600,3700]
}

df = pd.DataFrame(data)

# a) first 2 rows
print(df.head(2))

# b) last 3 rows
print(df.tail(3))

# c) check null values
print(df.isnull())

# d) replace null with mean
df["BidPrice"].fillna(df["BidPrice"].mean(), inplace=True)

# e) most expensive player
print(df.loc[df["BidPrice"].idxmax()])

# f) players per team
print(df["Team"].value_counts())
