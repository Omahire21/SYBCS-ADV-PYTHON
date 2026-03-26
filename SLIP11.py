#SLIP - 11
##Q.1
# create list
lst = [1,2,3,4,5,6,7,8,9,10]

# lambda with map
squares = list(map(lambda x: x*x, lst))

print("Original List:", lst)
print("Squares:", squares)

##Q.2
from flask import Flask, request

app = Flask(__name__)

tasks = []

@app.route("/", methods=["GET","POST"])
def home():
    if request.method == "POST":
        task = request.form["task"]
        tasks.append(task)

    html = """
    <h1>Task Manager</h1>

    <form method='post'>
        <input type='text' name='task' placeholder='Enter task'>
        <input type='submit' value='Add Task'>
    </form>

    <h2>Tasks:</h2>
    <ul>
    """

    for t in tasks:
        html += "<li>" + t + "</li>"

    html += "</ul>"

    return html

app.run()

##Q.2 - B
s = input("Enter a string: ")

words = s.split()

result = []

for w in words:
    if not any(v in w.lower() for v in "aeiou"):
        result.append(w)

result.sort()

print("Words without vowels:", result)
print("Total count:", len(result))
