##SLIP - 23
##Q.1
def productInfo(name, price=100):
    if price < 100:
        print("Product Name:", name)

# input
pname = input("Enter product name: ")

p = input("Enter price (press enter for default): ")

if p == "":
    productInfo(pname)
else:
    productInfo(pname, int(p))

##Q.2
import time
from datetime import datetime

# a) current local and UTC time
print("Local Time:", time.localtime())
print("UTC Time:", time.gmtime())

# b) ctime and gmtime
print("Current time using ctime():", time.ctime())
print("UTC using gmtime():", time.gmtime())

# c) accept date-time string
dt = input("Enter date-time (DD-MM-YYYY HH:MM:SS): ")

# d) parse and format
parsed = datetime.strptime(dt, "%d-%m-%Y %H:%M:%S")

print("Format 1:", parsed.strftime("%d/%m/%Y %H:%M"))
print("Format 2:", parsed.strftime("%A, %B %d %Y"))

##Q.2 - B
s = input("Enter string: ")

words = s.split()

result = []

for w in words:
    if not any(v in w.lower() for v in "aeiou"):
        result.append(w)

result.sort()

print("Words without vowels:", result)
print("Total count:", len(result))