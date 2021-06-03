"""
1.1 Write a Python Program(with class concepts) to find the area of the triangle using the below
formula.
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
Function to take the length of the sides of triangle from user should be defined in the parent
class and function to calculate the area should be defined in subclass.

1.2 Write a function filter_long_words() that takes a list of words and an integer n and returns
the list of words that are longer than n.

2.1 Write a Python program using function concept that maps list of words into a list of integers
representing the lengths of the corresponding words.
Hint: If a list [ ab,cde,erty] is passed on to the python function output should come as [2,3,4]
Here 2,3 and 4 are the lengths of the words in the list.

2.2 Write a Python function which takes a character (i.e. a string of length 1) and returns True if
it is a vowel, False otherwise.
"""

class Parent:
    def __init__(self):
        self.AB = int(input("AB : "))
        self.BC = int(input("BC : "))
        self.CA = int(input("CA : "))
    
class subclass(Parent):
    def __init__(self):
        super().__init__()
        self.S = (self.AB + self.BC + self.CA)/2
        self.area = (self.S * (self.S - self.AB)* (self.S - self.BC)* (self.S - self.CA)) ** 0.5
        print(self.area)

P = subclass()

#______________________________________

items = "asd asda ew we fafe afafeaf feaf adaas sd s fa rqaa qeq".split()

def filter_long_words(lst,n):
    lst1 = []
    for i in lst:
        if fun_filter(i,n): lst1.append(i)
    return lst1

fun_filter = lambda a,n: len(a) > n

print (filter_long_words(lst=items,n=3)) 

#______________________________________
items = "asd asda ew we fafe afafeaf feaf adaas sd s fa rqaa qeq".split()
def f(lst):
    lst1 = [len(i) for i in lst]    
    return lst1

print (f(lst=items))
#______________________________________
vowels = list("aeiouAEIOU")
def f(x):
    return x in vowels

print(f(input("Enter a character: ")))
