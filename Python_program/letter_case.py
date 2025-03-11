#!/usr/bin/python3.12
print("*****************letter case function*****************\n")
print("******************isalnum function********************\n")

print("*******************isupper function*******************\n")
string1="HELLO MANISH"

string2=string1.isupper()# true
print(string2)

string1="HELLO manish"

string2=string1.isupper()# false
print(string2)

string1="HELLO8478918409"

string2=string1.isupper()# true
print(string2)

string1="8478918409"
string2=string1.isupper()# false
print(string2)

string1="HELLoklafklkf"
string2=string1.isupper()# false
print(string2)


print("**************islower function*************************\n")
string1="manish kumar maurya"

string2=string1.islower()# true
print(string2)

string1="HELLO manish"

string2=string1.islower()# false
print(string2)

string1="manish8478918409"

string2=string1.islower()# true
print(string2)

string1="8478918409"
string2=string1.islower()# false
print(string2)

string1="HELLoklafklkf"
string2=string1.islower()# false
print(string2)



print("********************upper function************************\n")
string1="manish kumar maurya"

string2=string1.upper()# it will convert all lower lettr in upper
print(string2)

string1="HELLO manish"

string2=string1.upper()# 
print(string2)

string1="manish8478918409"

string2=string1.upper()# 
print(string2)

string1="8478918409"
string2=string1.upper()# 
print(string2)

string1="HELLoklafklkf"
string2=string1.upper()# 
print(string2)


print("**********************lower function***************\n")
string1="manish kumar maurya"

string2=string1.lower()# it will convert all upper lettr in lower
print(string2)

string1="HELLO manish"

string2=string1.lower()# 
print(string2)

string1="manish8478918409"

string2=string1.lower()# 
print(string2)

string1="8478918409"
string2=string1.lower()# 
print(string2)

string1="HELLoklafklkf"
string2=string1.lower()# 
print(string2)


print("***************title function**************************\n")
string1="manish kumar maurya"

string2=string1.title()# it will change all starting letter in capital
print(string2)

string1="HELLO manish"

string2=string1.title()# 
print(string2)

string1="manish8478918409"

string2=string1.title()# 
print(string2)

string1="8478918409"
string2=string1.title()# 
print(string2)



print("*****************swapcase function************************\n")
string1="manish kumar maurya"

string2=string1.swapcase()# it will change all lower to upper and all upper to lower
print(string2)

string1="HELLO manish"

string2=string1.swapcase()# 
print(string2)

string1="manish8478918409"

string2=string1.swapcase()# 
print(string2)

string1="8478918409"
string2=string1.swapcase()# 
print(string2)

#********************************************************************************

print("**********************center function*********************\n")
string1="manish kumar maurya"

string2=string1.center(50)# it will shift at center side
print(string2)

print(string1.center(70))


string1="HELLO manish"
print('****string1.center(50,"#")**it will add both side #********\n')
string2=string1.center(50,"#")#after string both side # will add
print(string2)

string1="manish8478918409"
print('****string1.center(50,"#")**it will add both side 5 *******\n')
string2=string1.center(75,"5")# after string both side 5 will add
print(string2)

#string1="manish"
#string2=string1.center(50,"maurya")# maurya is 6 character fill character not more than one character
#print(string2)


print("*********************ljust function************************\n")
string1="manish kumar maurya"
print('******string1.ljust(50)** after string 50 space will add***\n')
string2=string1.ljust(50)#after string1 50 space will come
print(string2,"hello")# after string1 50 space then after hello will come

string1="HELLO manish"
print(string1)
print('***string1.ljust(50,"#")after string right side # will add**\n')
string2=string1.ljust(50,"#")#after string  # will add
print(string2,"hi")#after string1 til 50 #will come then after hi will come

string1="                   manish8478918409"
print(string1)
print('***string1.ljust(75,"5")after string 5 will add**\n')
string2=string1.ljust(75,"5")# #after string 5 will add
print(string2,"manish kumar maurya")#after string1 til 75 5 will come then after manish kumar maurya will come



print("**********************rjust function**********************\n")
string1="manish kumar maurya"

string2=string1.rjust(50)# string will shifted right side left side will be space added
print(string2,"hello")# after string  hello will come

string1="HELLO manish"
print(string1)
string2=string1.rjust(50,"#")#string will shifted right side left side # will added
print(string2,"hi")#after string1 til 50 #will come then after hi will come

string1="                   manish8478918409"
print(string1)
string2=string1.rjust(75,"5")#string will shift right side and space also will added and left side 5 will added
print(string2,"manish kumar maurya")#after string1  manish kumar maurya will come





print("***********************find function**********************\n")
string1="manish kumar maurya"
string2=string1.find("a")#if a is in string then it will show index value of that character
print(string2)

for i in string1:
    print(f"{i}={string1.find(i)}")#it will print all character index value 
                            #repeated character index will show first time repetation index
print()
string1="manish kumar maurya"
string2=string1.find("f")#if character is not in string then it will print -1
print(string2)



print("******************rfind function**************************\n")
string1="manish kumar maurya"
string2=string1.rfind("a")#if a is in string then it will show index value in revers order of that character
print(string2)

for i in string1:
    print(f"{i}={string1.rfind(i)}")#it will print all character index value in revers order
                            #repeated character index will show first time repetation index
print()
string1="manish kumar maurya"
string2=string1.rfind("f")#if character is not in string then it will print -1
print(string2)
