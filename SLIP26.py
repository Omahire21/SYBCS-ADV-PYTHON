## SLIP - 26
##Q.1
s = input("Enter string: ")

# remove whitespaces
s = s.replace(" ", "")

print("Modified string:", s)

##Q.2
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

##Q.2 - B
import pandas as pd

data = {
"Label":["Pencil","Pencil","Pen","Pen","Eraser"],
"Company":["Apsara","Natraj","Cello","Parkar","Apsara"],
"Count":[15,20,25,35,20],
"Price":[250,200,600,900,300]
}

df = pd.DataFrame(data)

# a) rows with Pencil
print(df[df["Label"]=="Pencil"])

# b) change Eraser count to 25
df.loc[df["Label"]=="Eraser","Count"] = 25

# c) Company and Price columns
print(df[["Company","Price"]])

# d) rows with Pencil and Pen
print(df[df["Label"].isin(["Pencil","Pen"])])

# e) add Colour column
df["Colour"] = ["Red","Red","Blue","Blue","White"]

print(df)