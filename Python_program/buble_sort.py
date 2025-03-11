#!/usr/bin/python3.12

print("******************buble sort********************\n")
#buble sort 
value=[9,8,7,6,5,4,3,2,1,0]
l=len(value)
count_i=0
count_j=0
for i in range(l-1):
  count_i +=1
  for j in range(l-1):
     count_j +=1
     if(value[j+1]<value[j]):
        value[j+1],value[j]=value[j],value[j+1]

  print("sorted:",value,count_i,count_j)


print("***************#buble sort with user input*********\n")

#buble sort with user input
n=int(input("enter number of element:"))
value =[]
for i in range(0,n):
   a=int(input("enter array element:"))
   value.append(a)
  #print("array elements",value)
   l=len(value)

   count_i=0
   count_j=0
for i in range(l-1):
  count_i +=1
  for j in range(l-1):
     count_j +=1
     if(value[j+1]<value[j]):
        value[j+1],value[j]=value[j],value[j+1]

  print("sorted:",value,count_i,count_j)

