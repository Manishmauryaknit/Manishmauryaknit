#!/usr/bin/python3.12

print("**recursive print one one string in one one line**\n")

name=["saurabh","atul","ramudu",["raju","sandhya","anusha",["manish","sairam","anuradha","mamatha"]]] 
def recursiv(name):
  for i in name:
    if(isinstance(i,list)):
        recursiv(i)
        
    else:
        print(i)
recursiv(name)

#***********************************************
print("****************method 2************************\n")

 #isinstance is
a=[1,5,3,3,7,8,["manish","maurya"]]
b={"hello":5,"manish":7}
if(isinstance(a,list)):
    print(a)
    for i in a:
        print(i)
if(isinstance(b,dict)):
    print(b)
    for j in b:
      print(j)
#***********************************************


print("******************method 3***********************\n")
names=["saurabh","atul","ramdu",["raju","manish","ajit",["soni","priyanka","vibhor"]]]

def recursiv(names):
 for i in names:
    if(type(i)==type(names)):
         recursiv(i)
    else:
      print(i)
recursiv(names)



