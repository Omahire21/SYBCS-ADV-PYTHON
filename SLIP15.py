## SLIP - 15
## Q.1
import time

# current time in seconds
t = time.time()

# a) convert seconds to struct_time in UTC
utc_time = time.gmtime(t)
print("UTC struct_time:", utc_time)

# b) convert struct_time to formatted string
formatted = time.strftime("%d-%m-%Y %H:%M:%S", utc_time)
print("Formatted Time:", formatted)

##Q.2
from flask import Flask

app = Flask(__name__)

@app.route("/")
def library():
    return """
    <h1 style='text-align:center;'>City Library</h1>

    <table border="1">
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
            <td>Artificial Intelligence</td>
            <td>Andrew Ng</td>
        </tr>
    </table>

    <p style="color:blue; font-weight:bold;">
    Reading is to the mind what exercise is to the body.
    </p>
    """

app.run()

##Q.2 - B
import re

url = input("Enter URL: ")

pattern = r"https?://(www\.)?[a-zA-Z0-9\-]+\.[a-zA-Z]+"

if re.match(pattern, url):
    print("Valid URL")
else:
    print("Invalid URL")