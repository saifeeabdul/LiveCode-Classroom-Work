# LiveCode Classroom - Solution
# Batch: I.O.T 3 Sem Python Lab  2025-29
# Category: Live Lab Problems
# Question: Problem 1 (Create a class name Calculator)
# Score: Submitted (Evaluation Completed)
# Synced: Friday, November 20, 2026 at 9:29 AM

# Write your Python solution below
class Calculator:
    def add(self,a,b):
        print(f"The addition of 2 numbers are: {a}+{b}={a+b}")
    def sub(self,a,b):
        print(f"The sub of 2 numbers are: {a}-{b}={a-b}")
    def multiply(self,a,b):
        print(f"The multiply of 2 numbers are: {a}*{b}={a*b}")
    def divide(self,a,b):
        print(f"The division of 2 numbers are: {a}/{b}={a/b}")
obj1 = Calculator()
obj1.add(2,4)
obj1.sub(4,2)
obj1.multiply(2,4)
obj1.divide(6,3)

        
