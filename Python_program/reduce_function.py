#!/usr/bin/python3.12
'''
reduce function are takes 2 argument,
first argument is function
second argument is list or tuple
it reduce in single element acording to function
'''
print(__doc__)

from functools import reduce
import operator

inp1=int(input("enter range"))
list1=[]
for i in range(1,inp1):
   list1.append(i)
print("list1:",list1)
#sum of given number

list_num=reduce(lambda x,y:x+y,list1) # it will reduce in single value
print("sum of element",list_num)

#multiplication of given number
list_num=reduce(lambda x,y:x*y,list1) # it will reduce in single value
print("multiplication of element",list_num)

list_num=reduce(operator.add,list1) # it will reduce in single value
print("sum of element",list_num)

print(reduce(operator.concat, ["hello"," ","manish"]))

