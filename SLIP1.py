#SLIP - 1
#Q1. Write Python code to create a dictionary containing mobile names and their prices.Create DataFrame from this dictionary. Display the contents of DataFrame.#

import pandas as pd

# Creating dictionary
data = {
    "Mobile_Name": ["Samsung", "Redmi", "Realme", "iPhone"],
    "Price": [20000, 15000, 18000, 70000]
}

# Creating DataFrame
df = pd.DataFrame(data)

# Display DataFrame
print("Mobile DataFrame:")
print(df)

#Q.2-A
# cars module
def car_models():
    return ["Swift", "Baleno", "i20"]

# bikes module
def bike_models():
    return ["Pulsar", "Apache", "R15"]

# main program
print("Available Car Models:")
for car in car_models():
    print(car)

print("\nAvailable Bike Models:")
for bike in bike_models():
    print(bike)

## Q.2 - B
import os

files = os.listdir()

count = 0

for file in files:
    print(file)

    if file.endswith(".py"):
        count += 1

print("Total .py files:", count)

for file in files:
    if file.endswith(".py"):
        f = open(file, "r")
        print("\nContent of", file)
        print(f.read())
        f.close()
        break