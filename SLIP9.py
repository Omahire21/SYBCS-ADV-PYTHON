## SLIP 9
## Q.1
def even_generator(n):
    for i in range(2, n+1, 2):
        yield i

n = int(input("Enter value of n: "))

print("Even numbers up to", n)

for num in even_generator(n):
    print(num)

## Q.2
import pandas as pd

# Student 1 DataFrame
student1 = pd.DataFrame({
    "ID": ["S1","S2","S3","S4","S5"],
    "Name": ["Anita","Sakshi","Om","Raj","Kanika"],
    "Age": [18,23,20,21,20]
})

# Student 2 DataFrame
student2 = pd.DataFrame({
    "ID": ["S2","S4","S5","S6","S7"],
    "City": ["Pune","Nashik","Mumbai","Delhi","Nanded"],
    "Marks": [97,78,86,66,54]
})

print("Student 1 DataFrame")
print(student1)

print("\nStudent 2 DataFrame")
print(student2)

# join dataframes
student3 = pd.merge(student1, student2, on="ID")

print("\nJoined DataFrame")
print(student3)

## Q.2 -B
def armstrong(num):
    temp = num
    power = len(str(num))
    sum = 0

    while temp > 0:
        digit = temp % 10
        sum += digit ** power
        temp //= 10

    if sum == num:
        print("Armstrong Number")
    else:
        print("Not Armstrong")


def single_digit_sum(num):
    while num > 9:
        s = 0
        while num > 0:
            s += num % 10
            num //= 10
        num = s
    print("Single digit sum:", num)


n = int(input("Enter number: "))

armstrong(n)
single_digit_sum(n)