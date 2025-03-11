#!/usr/bin/python3.12
'''
map are taking argument function and one or more iterable element
it process on one one element and produce a list
map can take one or more iterable element but reduce are taking only one iterable argument
map produce one list but reduce produce one element
reduce or processing on 2 element but map or processing on one one element.
'''
print(__doc__)
print("*************map in python****************\n")
inp1=int(input("enter range"))
list1=[]
list2=[2,4,1,6,5,2,3]
for i in range(inp1):
   list1.append(i)

list_num=map(lambda x:x%2==0,list1) # it will print true and false
print("even",list(list_num))

list_num=list(map(lambda x:x%2,list1))    # it will print 1,and 0
print("odd",list_num)

list_num=list(map(lambda x,y:x+y,list1,list2))    # it will add 5 in each element
print("every element added 5",list_num)


list_num=tuple(map(lambda x:x%2==0,list1)) # it will print true and false
print("even",list_num)

list_num=tuple(map(lambda x:x%2,list1))    # it will print 1,and 0
print("odd",list_num)

list_num=tuple(map(lambda x:x+5,list1))    # it will add 5 in each element
print("every element added 5",list_num)

