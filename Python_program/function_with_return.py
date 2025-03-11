#!/usr/bin/python3.12

print("**** function with return type without argument ****\n")

def display():
    a=30
    b=50
    if(a<b):
      print("welcome in digicomm")
      return a
    else:
      print("welcome dv engineer")
      return b
display() #it will print 
print(display())#it will print and return return type value


#******************************************************************

print("**********multiple function inside one function ******\n")

def add(a,b):
   c=a+b
   return c


def sub(a,b):
    if(a>b):
      c=a-b 
      return c
    else:
      c=b-a
      return c

def fun(a,b):
  if(a==b):
    c=add(a,b)+sub(a,b)
    print(c)
  else:
    c=add(a,b)-sub(a,b)
    print(c)
    
inp1=int(input("enter input1:"))
inp2=int(input("enter input2:"))
fun(inp1,inp2)
print(fun(inp1,inp2))


