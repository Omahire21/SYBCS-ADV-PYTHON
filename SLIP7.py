#SLIP - 7
#Q.1
import re

s = input("Enter a string: ")

# remove special characters
clean = re.sub(r'[^A-Za-z\s]', '', s)

# extract words starting with capital letter
words = clean.split()

print("Words starting with capital letter:")
for w in words:
    if w[0].isupper():
        print(w)

print("Modified String:", clean)

#Q.2
from flask import Flask

app = Flask(__name__)

@app.route("/")
def library():
    return """
    <h1 style='text-align:center;'>City Library</h1>

    <table border='1'>
        <tr>
            <th>Title</th>
            <th>Author</th>
        </tr>
        <tr>
            <td>Python Programming</td>
            <td>Guido van Rossum</td>
        </tr>
        <tr>
            <td>Data Science</td>
            <td>Joel Grus</td>
        </tr>
        <tr>
            <td>AI Basics</td>
            <td>Andrew Ng</td>
        </tr>
    </table>

    <p style='color:blue; font-weight:bold;'>
    Reading is to the mind what exercise is to the body.
    </p>
    """

app.run()

#Q.2 - B
filename = input("Enter file name: ")

try:
    f = open(filename, "r")
    content = f.read()
    f.close()

    # copy to new file
    newfile = "copy.txt"
    f2 = open(newfile, "w")
    f2.write(content)
    f2.close()

    # display new file
    f3 = open(newfile, "r")
    text = f3.read()
    print("Content of new file:\n", text)

    print("Characters:", len(text))
    print("Words:", len(text.split()))
    print("Lines:", len(text.split("\n")))

    f3.close()

except FileNotFoundError:
    print("File does not exist")