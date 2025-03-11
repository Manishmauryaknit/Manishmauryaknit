#!/usr/bin/python3.12

print("**************** break and continue*******************\n")
# break and continue 
n=int(input("enter number"))
for i in range(n):
     if(i==5):
       break # it will break at 5
     print("break state",i)

for j in range(n):
    if(j==3):
     continue
    print("continue state",j)


#************************ fizz and buzz**************************************************

a=int(input("enter number"))

if(a%3==0 and a%7==0):
    print("fiz buzz")

elif(a%3==0):
  print("fizz")

elif(a%7==0):
  print("buzz")
else:
  print("bye bye")


  #*************************************************************

print("***********type() function***********************\n")

a="hello everyone"
b=[1,2,3,5,4,8]
c={"hello","manish","maurya"}
d=123113
e=1231.2
f={2:"hello",4:"hi"}
g=223**2
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
