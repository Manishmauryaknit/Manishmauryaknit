#!/usr/bin/python3.12
''' this python code contain lambda function as recursion.
    using recursion i wrote addition of list element.
    factorial of given number.
    some of number from zero to till that number. 
    '''

print(__doc__)

print("******************lambda function use as recursion*************************\n")
print("**********************addition of list*************************************\n")

list = [1, 2, 3, 4,5 ]
f = lambda l: l[0] if len(l) == 1 else l[0] + f(l[1:])
sum = f(list)
print(sum)



print("**********************factorial of number***********************************\n")

num =int(input("enter input number"))
f = lambda n: 1 if n<=1 else n * f(n-1)
fact = f(num)
print(fact)

print("**********************addition of number************************************\n")
num =int(input("enter input number"))
f = lambda n: n if n<1 else n + f(n-1)
sum = f(num)
print(sum)


