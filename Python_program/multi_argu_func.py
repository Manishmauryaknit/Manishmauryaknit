#!/usr/bin/python3.12

print("********function with multiple argument*******\n")
def multip(*num):
  print("number of argument:",len(num))
  for i in num:
    print("argument:",i)


multip(2,4,1,4,2,"h")


#********************************************************************

print("***function with multiple and default argument***\n")


def my_func(a,b,c=0,d=0):
  if(a and b and c and d):
    print("all argument is available",a,b,c,d)
  if(a and b and c):
    print("3 argument is available one will take default",a,b,c,d)
  else:
    print("two argument available two will take default argument",a,b,c,d)
 
my_func(3,4) 
my_func(2,3,5)
my_func(3,5,7,8)


#*******************************************************************

print("function with multiple argument multiple combination and default argument\n")

def my_func(a,b,c=0,d=0):
    e=a+b+c+d
    print("arg:",a,b,c,d)
    return e

print("value with two argument and two default argument sum=",my_func(3,4)) # it will take 2 argument and two default argument

print("value with 3 argument one default argumet sum=",my_func(2,3,5))

print("value with 4 argument no default argument sum=",my_func(3,5,7,8))

print("argument with keyword sum=",my_func(b=5,a=6,d=7,c=8))

print("argument with keyword and default value sum=",my_func(a=5,b=6,d=8))

#print(" keyword positiona value sum=",my_func(a=5,5,d=8))#after keyword positional value will not take

#print(" keyword positiona value sum=",my_func(5,a=5,d=8))#here a two time pass that is wrong

#print(" keyword positiona value sum=",my_func(a=5,5,d=8))#after keyword positional value will not take

#print(" keyword positiona value sum=",my_func(a=5,5,d=8))#after keyword positional value will not take

