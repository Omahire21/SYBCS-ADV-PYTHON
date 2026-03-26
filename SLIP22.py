##SLIP - 22
##Q.1
try:
    m = int(input("Enter value of m: "))
    n = int(input("Enter value of n: "))

    result = m / n
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed")

##Q.2
import pandas as pd

# Student 1
student1 = pd.DataFrame({
    "ID":["S1","S2","S3","S4","S5"],
    "Name":["Anita","Sakshi","Om","Raj","Kanika"],
    "Age":[18,23,20,21,20]
})

# Student 2
student2 = pd.DataFrame({
    "ID":["S2","S4","S5","S6","S7"],
    "City":["Pune","Nashik","Mumbai","Delhi","Nanded"],
    "Marks":[97,78,86,66,54]
})

print("Student 1:")
print(student1)

print("\nStudent 2:")
print(student2)

# merge
student3 = pd.merge(student1, student2, on="ID")

print("\nMerged DataFrame:")
print(student3)

#Q.2 - B
class FactorialSeries:
    def __init__(self,n):
        self.n = n
        self.i = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.i <= self.n:
            f = 1
            for j in range(1,self.i+1):
                f *= j
            self.i += 1
            return f
        else:
            raise StopIteration


n = int(input("Enter n: "))

for x in FactorialSeries(n):
    print(x)