## SLIP - 20
## Q.1
s = input("Enter string: ")

v = c = sp = 0

for ch in s:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            v += 1
        else:
            c += 1
    else:
        sp += 1

print("Vowels:", v)
print("Consonants:", c)
print("Special Symbols:", sp)

##Q.2
filename = input("Enter file name: ")
pos = int(input("Enter byte position: "))

try:
    f = open(filename,"r")

    f.seek(pos)

    print("Content from given position:")
    print(f.read())

    f.close()

except FileNotFoundError:
    print("File does not exist")

##Q.2 - B
import pandas as pd

data = {
"school":["S1","S2","S3","S4","S5","S6"],
"name":["Asha","Fransis","Charlie","David","Shyam","Eashel"],
"age":[12,12,13,14,12,16],
"height":[173,192,186,167,151,159],
"weight":[35,32,33,30,31,32],
"address":["Street1","Street2","Street3","Street4","Street5","Street6"]
}

df = pd.DataFrame(data)

# a) group by school
grp = df.groupby("school")

# b) type of groupby object
print(type(grp))

# c) mean, min, max of age
print(grp["age"].agg(["mean","min","max"]))

# d) students with weight > 32
print("Students weight > 32:", len(df[df["weight"]>32]))