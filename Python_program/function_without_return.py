#!/usr/bin/python3.12

print("**********python funtion without return**************")

def multi():
     a=200
     b=30
     c=a*b
     print(F"multiplication  of{a} and {b}=:{c}")
multi()     
print(multi()) # it will execute multi() function and retune None


#****************************************************************

print("*****function with argument without return************")

def addition(a,b):
   if(a>b):
       print("a is greater than b sum of a and b=",a+b)
   else:
       print("a is not greater than b sum of a and b=",a+b)
   
addition(9,7)
print(addition(3,9))

#******************************************************************

print("*****function with user input with argument***********")

def even_odd(num):
   if(num%2==0):
      print("number is even:",num)
   else:
      print("number is odd:",num)

# taking input from user
num=int(input("enter number:"))
# calling function
even_odd(num)

