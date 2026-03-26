##SLIP - 25
##Q.1
import random

suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
ranks = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]

deck = []

for s in suits:
    for r in ranks:
        deck.append(r + " of " + s)

random.shuffle(deck)

print("Cards obtained in 5 attempts:")

for i in range(5):
    print(deck[i])

##Q.2
def cal_interest(amount, year):
    rate = 0.05
    return amount * rate * year

def convert(amount):
    usd = amount * 0.012
    return usd


amt = float(input("Enter amount: "))
yr = int(input("Enter years: "))

print("Simple Interest:", cal_interest(amt, yr))

print("Amount in USD:", convert(amt))

##Q.2 - B
import re

url = input("Enter URL: ")

pattern = r"https?://(www\.)?[a-zA-Z0-9\-]+\.[a-zA-Z]+"

if re.match(pattern, url):
    print("Valid URL")
else:
    print("Invalid URL") 