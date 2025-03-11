#!/usr/bin/python3.12

print("*********************string.formating**************************************\n")

print("*****************using .format() type 1:***********************************\n")

string2="name {name},company{company},Email{Email}".format(name="Manish",company="Digicomm semiconductor",Email="manish@1234.com")
print(string2)

#************************************************************************************

print("*****************using .format() type 2:***********************************\n")

string2="name {0},company{1},Email{2}".format("Manish","Digicomm semiconductor","manish@1234.com")
print(string2)

#************************************************************************************

print("*****************using .format() type 3:***********************************\n")
string2="name {},company{},Email{}".format("Manish","Digicomm semiconductor","manish@1234.com")
print(string2)


#********************************************************************************

print("*****************using .format() type 4:***********************************\n")
name="Manish"
company="Digicomm semiconductor"
Email="manish@1234.com"
string2="name {0},company{1},Email{2}".format(name,company,Email)
print(string2)

#********************************************************************************
"""

name="Manish"
company="Digicomm semiconductor"
Email="[manish@123455.com"
string2="name {name},company{company},Email{Email}".format(name,company,Email)#it is not working
print(string2)
"""
#********************************************************************************

print("*****************string with format specifier***************************\n")
name="manish"
company="Digicomm"
age=26
print("name=%s,company=%s,age=%d"%(name,company,age))

print("name=%s,company=%s,age=%d"%("Maurya","Dcsemi",26))


#********************************************************************************

print("******************string with fstring***********************************\n")
name="manish"
company="Digicomm"
age=26
string2=f"name={name},company={company} age={age}"#fstrings instead of format specifier
print(string2)
 

print("********************fstring with operator*******************************\n")
a=50
b=6
value=f"a={a},b={b},c={a*b}"
print(value)

value=f"a={a},b={b},c={a**b}"
print(value)

value=f"a={a},b={b},c={a>b}"
print(value)

value=f"a={a},b={b},c={a and b}"
print(value)

value=f"a={a},b={b},c={a % b}" 
print(value)

value=f"a={a},b={b},c={a | b}"#a=50=b11010 b=6=b00110 c=54=b11110
print(value)

value=f"a={a},b={b},c={a & b}"#a=50=b11010 b=6=b00110 c=2=b00010
print(value)



#********************************************************************************


print("**********************fstring with lambda function**********************\n")
a=50
b=6

lam=lambda x,y:a%b                #lambda function declaration
value=f"a={a},b={b},c={lam(a,b)}" #calling lambda function inside fstring
print(value)
 


