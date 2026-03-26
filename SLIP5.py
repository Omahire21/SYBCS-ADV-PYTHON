##SLIP - 5
#Q.1
s = input("Enter a string: ")

words = s.split()

print("Words without vowels:")

for w in words:
    if not any(v in w.lower() for v in "aeiou"):
        print(w)

##Q.2
# account module
def open_account(name):
    print("Account created successfully for", name)

# loan module
def apply_loan(amount):
    print("Loan applied successfully for amount:", amount)

# main program
name = input("Enter account holder name: ")
amount = int(input("Enter loan amount: "))

open_account(name)
apply_loan(amount)

#Q.2 - B
m = int(input("Enter m: "))
n = int(input("Enter n: "))

primes = [x for x in range(m, n+1) if x > 1 and all(x % i != 0 for i in range(2, x))]

print("Prime numbers:", primes)