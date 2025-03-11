#!/usr/bin/python3.12

#numeric operation
x=10
y=7
print("***********************division*****************\n")
z=x/y
print("value of division/",z)# out put will be in decimal
z=x//y
print("value of division//",z)#output will be in integer


print("****************power****************************\n")
z=pow(x,5)
print("value of x**5",z)
print("value of x**3",x**3)


print("*********************absolute number*************\n")
print("absolute number",abs(-10))     #it will print 10
print("absolute number",abs(-50.234)) #it will print 50.234
print("absolute number",abs(50.634)) #it will print 50.634
print("absolute number",abs(10))      #it will print 10


print("**********************float value *****************\n")
z=float(x)
print("float value",z) #it will print 10.0
print("float value of 20",float(20)) # it will print 20.0


print("**********************round off *****************\n")
x=23.53538
z=round(x,2) # it will print 23.54
print("round off value",x,z)


print("************************integer value*************\n")
z=int(x)
print("int value",z)


print("************************ceil value*************\n")
import math
z=math.ceil(x)         #round off upper nearest value
print("ceil of x",x,z) # it will print 24 


print("************************floor value*************\n")
z=math.floor(x)              # round off lower nearest value
print("floor value of x",x,z)# it will print 23


print("************************ is ********************\n")
a=20
b=20
e="hello"
f="hello"

print("a is b",a is b)        #true will come
print("a is not b",a is not b)#false
print( "e is f",e is f)       #true
print("*******************_ underscore****************\n")
d=a+b
print(d)
#print(_*2)# it will work only in interective shell 


print("*********************int to binary*************\n")
print("value in binary",bin(d))     # it will print binary value of d variable
print("10 value in binary",bin(10)) # it will print binary value of 10


print("******************int to hexadecimal***********\n")
print("value in hex",hex(d))     # it will convert decimal value to hex
print("10 value in hex",hex(10))


#**********************************************************************************************************

x="manish"
y="maurya"
print("***********************string cancatination***************\n")
print(x,y)
print("x+y=",x+y)               #string cancatination
print("x*3=",x*3)               #it will print 3 time manish
print("x+kumar+y=",x+"kumar"+y) #it will print "manish kumar maurya"

print("***********************string with index*****************\n")
print("string:",x)
print("\n")
print("first element of strint",x[0])
print("last element of strint",x[-1])
print("3 to 4 element of string",x[2:5]) #2 is inclusive and 5 is exclusive
print("start from 3rd element of strint",x[3:])
print("start from last 4rd element of strint",x[-3:])
print("start from last 3rd end at -2 element of strint",x[-3:-1])
print("start from first element end at 2rd element of strint",x[:3])

print('hello\'manish')#hello'manish it will print, \ used as scape character
print(r'hello\'manish')#hello\'manish it will print,r represent raw string

print("*****************string print in multiple line************\n")

print("""manish
kumar
maurya""")# it will print in diffrent line


#****************************************************************************

print("********to byte convert little indian and big indian**********\n")
x=20
print("**************** int to byte big indian**********************\n")
print(x.to_bytes(2,'big'))#output will be b'\x00\x14'
print("**************** int to byte little indian*******************\n")
print(x.to_bytes(2,'little'))#output will be b'\x14\x00'
print("************from byte to int big indian**********************\n")
print(int.from_bytes(b'\x00\x14',byteorder='big'))#output will be 20
print("************from byte to int litlle indian*******************\n")
y=b'\x14\x00'
print(int.from_bytes(y,byteorder='little'))#output will be 20
