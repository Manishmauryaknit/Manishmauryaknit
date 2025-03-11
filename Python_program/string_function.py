#!/usr/bin/python3.12

print("*******************join function with string****************************\n")

string1="m","a","n","i","s","h","_","k","u","m","a","r","_","m","a","u","r","y","a"
string=("".join(string1))
print(string)

print("****************************join with " " ******************************\n")
string=(" ".join(string1))
print(string)

#join with _
print("****************************join with "'_'" ******************************\n")
string=("_".join(string1))
print(string)


print("*******************join function with list******************************\n")

list1=["m","a","n","i","s","h","_","k","u","m","a","r","_","m","a","u","r","y","a"]
list2=("".join(list1)) #it will give string
print(list2)

print("****************************join with " " ******************************\n")
#join with " "
list2=(" ".join(list1)) #it will give string
print(list2)



print("********************strip function**************************************\n")

string= "  hello manish   "
print("before strip:\n")
print(string)
print("after strip:\n")
print(string.strip()) #it will remove starting and ending space


#*******************************************************************************

string= "hello manish"
print("before strip:\n")
print(string)
print("after strip:\n")
print(string.strip("hello")) #it will remove starting all element and ending hello



#*******************************************************************************


string= "    hello manish     "
print("before strip:\n")
print(string)
print("after strip:\n")
print(string.strip("hello")) #it will not remove anything bcz space is there

string= "    hello manish     "
print("before strip:\n")
print(string)
print("after strip:\n")
print(string.strip("       hello       ")) #it will remove starting all element and ending hello and space also


#*******************************************************************************


print("********************replace function************************************\n")

string1="hello manish kumar maurya"
print(string1)
string2=string1.replace("hello","Hi")
print(string2)



print("*******************split function***************************************\n")

string1="hello manish kumar maurya"
print("before split:\n")
print(string1)
string2=string1.split()   #it split string with space
print("after split by space:\n")
print(string2)

string1="hello_manish_kumar_maurya"
print("before split:\n")
print(string1)
string2=string1.split("_")#it split string with _
print("after split by _:\n")
print(string2)

print("*******************isalnum function*************************************\n")

string1="hello manish kumar maurya"

string2=string1.isalnum() #false will come bcz string contain space it is not alphanumeric
print(string2)


string1="hello_manish"

string2=string1.isalnum() #false will come bcz string contain _ it is not alphanumeric
print(string2)

string1="hellomanish"
string2=string1.isalnum() #true  will come bcz string is aphabate
print(string2)

string1="hellomanish12342"
string2=string1.isalnum() #true  will come bcz string is aphanumeric
print(string2)

string1="12340989092"
string2=string1.isalnum() #true  will come bcz string is numeric
print(string2)


print("***********************isalpha function*********************************\n")

string1="hello manish kumar maurya"

string2=string1.isalpha() #false will come bcz string contain space 
print(string2)

string1="hello_manish"

string2=string1.isalpha() #false will come bcz string contain _ 
print(string2)

string1="hellomanish"
string2=string1.isalpha() #true  will come bcz string is aphabate
print(string2)

string1="hellomanish12342"
string2=string1.isalpha() #false  will come bcz string is aphanumeric
print(string2)

print("*******************isdigit function*************************************\n")

string1="hello manish kumar maurya"

string2=string1.isdigit() #false will come bcz string not contain digit 
print(string2)

string1="hello_manish"

string2=string1.isdigit() #false will come bcz string contain _ not contain digit
print(string2)

string1="hello1313manish"
string2=string1.isdigit() #false  will come bcz string not contain only digit
print(string2)

string1="898812342"
string2=string1.isdigit() #TRUE will come bcz string is numeric
print(string2)


print("**************************isspace function******************************\n")

string1=" "

string2=string1.isspace() #true will come bcz string contain only space
print(string2)

string1="hello_manish"

string2=string1.isspace() #false will come bcz string contain _
print(string2)

string1="hello1313manish"
string2=string1.isspace() #false  will come bcz string contain  alphabate and digit
print(string2)

string1="898812342"
string2=string1.isspace() #false  will come bcz string is aphanumeric
print(string2)


print("*************************istitle function*******************************\n")

string1="Manish Kumar Maurya"

string2=string1.istitle() #true will come because M is capital letter
print(string2)

string1="hello_manish"

string2=string1.istitle()# false
print(string2)


