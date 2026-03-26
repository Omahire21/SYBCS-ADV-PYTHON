##SLIP - 4
#Q.1
import random

# create list
lst = [10, 20, 30, 40, 50]

print("Original List:", lst)

# shuffle list
random.shuffle(lst)

print("Shuffled List:", lst)

#Q.2
import pandas as pd

data = {
    "Company": ["Apsara","Natraj","Cello","Parkar","Apsara"],
    "Count": [15,20,25,35,20],
    "Pencil": ["Pencil","Pen","Pen","Eraser","Pencil"],
    "Price": [250,200,600,900,300]
}

df = pd.DataFrame(data)

print("Original DataFrame")
print(df)

# a) rows with label Pencil
print("\nRows with Pencil:")
print(df[df["Pencil"]=="Pencil"])

# b) change Eraser count to 25
df.loc[df["Pencil"]=="Eraser","Count"] = 25
print("\nAfter updating Eraser count:")
print(df)

# c) only Company and Price columns
print("\nCompany and Price columns:")
print(df[["Company","Price"]])

# d) rows with Pencil and Pen
print("\nRows with Pencil and Pen:")
print(df[df["Pencil"].isin(["Pencil","Pen"])])

# e) rename Count to Quantity
df.rename(columns={"Count":"Quantity"}, inplace=True)
print("\nAfter renaming column:")
print(df)

#Q.2 - B
# create file and write 5 friends
f = open("friends.txt","w")

f.write("Rahul Kumar\n")
f.write("Amit Sharma\n")
f.write("Neha Patel\n")
f.write("Riya Singh\n")
f.write("Karan Mehta\n")

f.close()

# display file
f = open("friends.txt","r")
print("File Contents:")
print(f.read())
f.close()

# append 5 more friends
f = open("friends.txt","a")

f.write("Ankit Verma\n")
f.write("Priya Jain\n")
f.write("Sahil Khan\n")
f.write("Pooja Gupta\n")
f.write("Rohit Das\n")

f.close()

# display modified file
f = open("friends.txt","r")
print("\nModified File Contents:")
print(f.read())
f.close()