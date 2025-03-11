#!/usr/bin/python3.12

print("*************insertion sort *********************\n")

value=[9,8,7,6,5,4,3,2,1,0]
l=len(value)
temp=0;
for i in range(1,l):
  temp=value[i]
  j=i-1
  while j>= 0 and temp < value[j]:
      value[j+1]=value[j]
      j=j-1
      value[j+1]=temp
  print(value)
 

print("**********insertion sort with user input**********\n")

n=int(input("enter number of element:"))
value =[]
for i in range(0,n):
   a=int(input("enter array element:"))
   value.append(a)
   #print("array elements",value)
   l=len(value)
   print(value)
   temp=0;
for i in range(1,l):
  temp=value[i]
  j=i-1
  while j>= 0 and temp < value[j]:
      value[j+1]=value[j]
      j=j-1
      value[j+1]=temp
  print(value)

