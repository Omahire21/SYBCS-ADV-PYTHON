##SLIP - 17
##Q.1
s = input("Enter string: ")

# replace space with colon
s = s.replace(" ", ":")

# replace comma with dot
s = s.replace(",", ".")

print("Modified string:", s)

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
def armstrong(n):
    temp = n
    power = len(str(n))
    s = 0

    while temp > 0:
        digit = temp % 10
        s += digit ** power
        temp //= 10

    if s == n:
        print("Armstrong Number")
    else:
        print("Not Armstrong")


def single_digit_sum(n):
    while n > 9:
        s = 0
        while n > 0:
            s += n % 10
            n //= 10
        n = s
    print("Single digit sum:", n)


num = int(input("Enter number: "))

armstrong(num)
single_digit_sum(num)