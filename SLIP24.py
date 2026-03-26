##SLIP - 24
##Q.1
import re

s = input("Enter string: ")

nums = re.findall(r"\d+", s)

print("Extracted Numbers:", nums)

##Q.2 
def check_pass_fail(marks):
    if marks >= 40:
        return "Pass"
    else:
        return "Fail"


n = int(input("Enter number of students: "))

pass_count = 0
fail_count = 0

for i in range(n):
    m = int(input("Enter marks: "))
    result = check_pass_fail(m)

    print("Result:", result)

    if result == "Pass":
        pass_count += 1
    else:
        fail_count += 1

print("Total Passed:", pass_count)
print("Total Failed:", fail_count)

##Q.2 -B
from flask import Flask

app = Flask(__name__)

@app.route("/")
def college():
    return """
    <h1 style='text-align:center;'>XYZ College</h1>

    <h2>Courses</h2>
    <ul>
        <li>BSc Computer Science</li>
        <li>BCA</li>
        <li>BBA</li>
        <li>MCA</li>
    </ul>

    <img src="https://upload.wikimedia.org/wikipedia/commons/1/1a/College_building.jpg" width="300">
    """

app.run()