#!/usr/bin/python3.12
print("***************selection sort *********************\n")

array=[2,1,5,3,8,8,0,5]
l=len(array)
for i in range(0,l-1):
     temp=i
     for j in range(i+1,l):
        if(array[j]<array[temp]):
          temp=j
     array[i],array[temp]=array[temp],array[i]
     print(array)
        

print("***********selection sort with user input********\n")

n=int(input("enter number of elemnt:"))
array=[]
for i in range(n):
   el=int(input("enter element:"))
   array.append(el)
l=len(array)
print("unsorted:",array)
for i in range(0,l-1):
    temp=i
    for j in range(i+1,l):
        if(array[j]<array[temp]):
         temp=j
    array[i],array[temp]=array[temp],array[i]
    print("sorted:",array)


