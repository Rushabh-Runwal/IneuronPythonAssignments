"""
1.1 Write a Python Program to implement your own myreduce() function which works exactly
like Python's built-in function reduce()

1.2 Write a Python program to implement your own myfilter() function which works exactly
like Python's built-in function filter()

2. Implement List comprehensions to produce the following lists.
Write List comprehensions to produce the following Lists

['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz']
[[2], [3], [4], [3], [4], [5], [4], [5], [6]] 
[[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]
[(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]

"""

items = [1, 24, 17, 14, 9, 32, 2]

def myreduce(fun,lst):
    for i in range(len(lst)-1):
        lst = [fun(lst[0],lst[1])] + lst[2:]
    return lst[0]
fun_reduce = lambda a,b: a if (a > b) else b # a+b

print (myreduce(fun=fun_reduce,lst=items)) 

#______________________________________________

def myfilter(fun,lst):
    lst1 = []
    for i in lst:
        if fun(i): lst1.append(i)
    return lst1

fun_filter = lambda a: a < 15
print (myfilter(fun=fun_filter,lst=items)) 

#______________________________________________

lst1 = list("xyz")
print(*[ "".join([i]*j) for i in lst1 for j in range(1,5) ])
print(*[ "".join([i]*j) for j in range(1,5) for i in lst1 ])
print(*[ [j+i] for j in range(3,6) for i in range(-1,2) ])
print(*[ [ i+j for j in range(4)] for i in range(2,6) ])
print(*[  (i,j) for j in range(1,4) for i in range(1,4) ])