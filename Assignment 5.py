"""
1. Write a function to compute 5/0 and use try/except to catch the exceptions.
2. Implement a Python program to generate all sentences where subject is in
["Americans", "Indians"] and verb is in ["Play", "watch"] and the object is in
["Baseball","cricket"].
Hint: Subject,Verb and Object should be declared in the program as shown below.
subjects=["Americans ","Indians"]
verbs=["play","watch"]
objects=["Baseball","Cricket"]
Output should come as below:
Americans play Baseball.
Americans play Cricket.
Americans watch Baseball.
Americans watch Cricket.
Indians play Baseball.
Indians play Cricket.
Indians watch Baseball.
Indians watch Cricket.
"""
def fun(a,b):
    c = None
    try:
        c = a/b
    except ZeroDivisionError:
        print("Divide by zero error")
    finally:
        print(c)
fun(int(input("a: ")),int(input("b: ")))

#___________________________________________


subjects=["Americans","Indians"]
verbs=["play","watch"]
objects=["Baseball","Cricket"]

for i in subjects:
    for j in verbs:
        for k in objects:
            print(i,j,k,end=".\n")