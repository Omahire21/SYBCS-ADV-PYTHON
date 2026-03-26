# SLIP - 6
# Q.1
try:
    a = input("Enter first number: ")
    b = input("Enter second number: ")

    if not a.isnumeric() or not b.isnumeric():
        raise TypeError("Input must be numeric")

    a = int(a)
    b = int(b)

    print("Sum:", a + b)

except TypeError as e:
    print(e)

## Q.2
import pandas as pd

data = {
    "Label": ["Pencil","Pencil","Pen","Pen","Eraser"],
    "Company": ["Apsara","Natraj","Cello","Parkar","Apsara"],
    "Count": [15,20,25,35,20],
    "Price": [250,200,600,900,300]
}

df = pd.DataFrame(data)

print("Original DataFrame")
print(df)

# a) rows with Pencil
print("\nRows with Pencil:")
print(df[df["Label"]=="Pencil"])

# b) change Eraser count to 25
df.loc[df["Label"]=="Eraser","Count"] = 25

# c) only Company and Price
print("\nCompany and Price:")
print(df[["Company","Price"]])

# d) rows with Pencil and Pen
print("\nRows with Pencil and Pen:")
print(df[df["Label"].isin(["Pencil","Pen"])])

# e) delete Count column
df = df.drop("Count", axis=1)

print("\nAfter deleting Count column:")
print(df)

#Q.2 - B
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1 style='text-align:center;'>Om Ahire</h1>
    
    <h2>Qualification</h2>
    <ul>
        <li>SYBSc Computer Science</li>
        <li>SPPU University</li>
    </ul>

    <marquee>Skills: Python, Flutter, AI Development</marquee>
    """

app.run()