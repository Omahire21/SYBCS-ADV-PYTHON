## SLIP -8
## Q.1
def area(radius):
    return 3.14 * radius * radius

r = float(input("Enter radius: "))

result = area(r)

print("Area of Circle:", result)

## Q.2
import random

# list
lst = [10,20,30,40,50]

# string
s = "PYTHON"

# tuple
t = (1,2,3,4,5)

print("Random elements from list:", random.sample(lst,3))

print("Random elements from string:", random.sample(s,3))

print("Random elements from tuple:", random.sample(t,3))

##Q.2 - B
from flask import Flask

app = Flask(__name__)

@app.route("/")
def college():
    return """
    <h1 style='text-align:center;'>XYZ College</h1>

    <h2>Courses Available</h2>
    <ul>
        <li>BSc Computer Science</li>
        <li>BCA</li>
        <li>BBA</li>
        <li>MCA</li>
    </ul>

    <img src="https://upload.wikimedia.org/wikipedia/commons/1/1a/College_building.jpg" width="300">
    """

app.run()