#SLIP - 3
#Q.1
try:
    m = int(input("Enter value of m: "))
    n = int(input("Enter value of n: "))

    result = m / n
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

## Q.2
# factorial function
def factorial(n):
    f = 1
    for i in range(1, n+1):
        f = f * i
    return f

# power dictionary
power = {
    2: 4,
    3: 9,
    4: 16,
    5: 25
}

# vowels list
vowels = ['a', 'e', 'i', 'o', 'u']

# accept number
n = int(input("Enter number: "))

# factorial
print("Factorial:", factorial(n))

# power
print("Power:", power.get(n, "Not available"))

# second vowel
print("Second vowel:", vowels[1])

##Q.2 - B
filename = input("Enter file name: ")

try:
    f = open(filename, "r")

    content = f.read()

    print("File Content:\n", content)

    characters = len(content)
    words = len(content.split())
    lines = len(content.split("\n"))

    print("Characters:", characters)
    print("Words:", words)
    print("Lines:", lines)

    f.close()

except FileNotFoundError:
    print("File does not exist.")