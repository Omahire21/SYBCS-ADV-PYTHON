## SLIP - 10
## Q.1
import pandas as pd

# list of 10 integers
data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

df = pd.DataFrame(data, columns=["Numbers"])

print("DataFrame:")
print(df)

print("Sum:", df["Numbers"].sum())
print("Mean:", df["Numbers"].mean())
print("Median:", df["Numbers"].median())
print("Mode:", df["Numbers"].mode()[0])
print("Standard Deviation:", df["Numbers"].std())

##Q.2
# interest function
def cal_interest(amount, year):
    rate = 0.05
    si = amount * rate * year
    return si

# currency conversion function
def convert(amount):
    usd = amount * 0.012
    return usd

amount = float(input("Enter amount: "))
year = int(input("Enter years: "))

print("Simple Interest:", cal_interest(amount, year))

print("Amount in USD:", convert(amount))

## Q.2 - B
class FactorialSeries:
    def __init__(self, n):
        self.n = n
        self.i = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.i <= self.n:
            f = 1
            for j in range(1, self.i + 1):
                f *= j
            self.i += 1
            return f
        else:
            raise StopIteration

n = int(input("Enter n: "))

print("Factorial series:")
for x in FactorialSeries(n):
    print(x)