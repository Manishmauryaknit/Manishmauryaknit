#!/usr/bin/python3.12

print("****lanbda function in python****************\n")

x=int(input("enter input x:"))
y=int(input("enter input y:"))


a=lambda x,y:x+y  #lamda function declaration

b=lambda x:print("odd number") if x%2 else print("even number")

c=lambda x:print("number is greater than 10") if x>10 else print("number is less than 10")

print(a)          #it will print address of lambda function

print("sum of x and y:",a(x,y))  #lamda function calling

print("address of lambda:",a,lambda x,y:x+y) #both address will be diffrent 

print(b(x))  #it will print even and odd number

print(c(x)) #it will print number greater than 10 and less than 10

#****************************************************************

print("**********lambda with default value*********************\n")

fc=lambda a=0,b=1,c=2,d=3:a+b+c+d  #lamda function

print(fc())#it will execute with default value

print(fc(2,3))# two value it will take default

print(fc(5,3,7))#one value it will take default 

print(fc(3,5,2,1))# no default value will take

#print(fc(a=2,2,4,5)) #after keywrod positional value will not accept 
print(fc(2,3,5,d=10))#takeing 3 positional argument and one keywords argument
 
print(fc(a=3,b=3,c=5,d=20))# all argument is keywords argument



print("\n")

print("******inside lambda function user define function**********\n")

def add(x,y):
    return x+y

#inside lambda calling useer defined function

c=lambda x,add:x+add
print(c(x,add(x,y)))
#c=lambda x,add:x+add(x,y)
#print(c(x,lambda x,y:x+y)) 





