print("***************************string in string******************************\n")
#finding string in string
string1="manish_kumar_maurya"
string2="maurya"
if string2 in string1:
    print("yes string available")
else:
    print("string is not available")

print("*************************************************************************\n")
string1="manish_kumar_maurya"
if "manish" in string1:
    print("yes string available")
else:
    print("string is not available")


print("****************searching string in list*********************************\n")

list1=["manish","kumar","maurya"]
string2="maurya"

if string2 in list1:
    print("in->","yes string2 available")
else:
    print("in->","string2 is not available")


if string2 not in list1:
    print("not in->","yes string2 is not available")
else:
    print("not in->","string2 is  available")

print("*************************************************************************\n")

list1=["manish","kumar","maurya"]

if "kumar" in list1:
    print("in list1 ->","yes string kumar available")
else:
    print("in list1 ->","string is kumar not available")

#****************************************************************************************************************

print("******************string access with index value*************************\n")

string1="manish_kumar_maurya"

print(string1[0])# it will print index 0 letter
print(string1[1:])# it will print from 1st index 
print(string1[0::2])# it will skip one one word
print(string1[0:20:2])# it will skip one one word
print(string1[::-1])# it will print in reverse order


print("**********************string max min*************************************\n")
print("****************it will print max ascii value of letter******************\n")

string1="manish_kumar_maurya"

print(len(string1))# it will print length of string

print(max(string1)) #it will print max ascii value letter that is y
print(min(string1)) #it will print min ascii value letter that is _



print("*****************printing ascii to character with ascii value************\n")
list2=[]
for i in range(128):
    print("ascii->",i,"letter->",chr(i))
    list2.append(chr(i))#ascii to character
print(" characteer list2=:",list2)

print("***************printing character to ascii*******************************\n")
    
for i in list2:
    print("char",i,"ascii",ord(i)) #it will return ascii code of given character
  

#********************************************************************************

print("***************************index function*******************************\n")

print("************************find index of string****************************\n")

string1="manish_kumar_maurya"
print(string1.index("m"))#it will return index of m first letter in given string output=0
print(string1.index("m",5))#it will return index of m after 5 index in given string output=9

print(string1.index("m",10,19))#it will return index of m after 10 index and befor 19index
                               #letter in given string output=13
                            
#print(string1.index("p"))#if letter is not there then error will come p is not available in given string

print("**********************find rindex of string*****************************\n")

string1="manish_kumar_maurya"
print(string1.rindex("m"))#it will return revers index of m last first letter in given string output=13
print(string1.rindex("m",5))#it will return revers index of m after 5 index in given string output=13
print(string1.rindex("m",10,19))#it will return revers index of m after 10 index and befor 19index 
                                #letter in give string output=13
                               
print("***********************find index of list*******************************\n")
list2=[]
for i in range(65,91):
    list2.append(chr(i))#it convert ascii  to charcter and append in list
print(list2) #it will print all A_Z letter

print(list2.index("M"))#it will return index of M in given list
print(list2.index("Z"))#it will return index of M in given list
#print(list2.rindex("M"))# rindex is not working for list


print("********************count function in string****************************\n")

string1="manish_kumar_maurya"

print(string1.count("m"))      # it will return number of m in given string output =13
print(string1.count("k"))      # it will return number of k in given string output =1
print(string1.count("m",5))    # it will return number of m after 5index in given string output =2
print(string1.count("m",10,19))# it will return number of m after 5 index and befor index 19 in
                               #given string output =1

print(string1.count("k",10,19))# it will return number of k in given range output=0
print(string1.count("p"))      # it will return number of p in string output=0


