"""
1. Write a program which accepts a sequence of comma-separated numbers from console  and generate a list. 
1. Create the below pattern using nested for loop in Python. 
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
* 

2. Write a Python program to reverse a word after accepting the input from the user.
Sample :
Input word: ineuron 
output: norueni
"""
l = input().split(',')
print(l)
#_______________________________________________
j = 1
for i in range(9):
    if i < 5 :print("".join(["* "]*(i+1)))
    else: 
        print("".join(["* "]*(i-j)))
        j+=2
#_______________________________________________
rev = "".join(list(input())[::-1])
print(rev)