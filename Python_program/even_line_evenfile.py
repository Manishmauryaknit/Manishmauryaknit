#!/usr/bin/python3.12

def even_odd_line(input_file,even_file,odd_file):
    with open(input_file,"r") as infile,\
         open(even_file,"w") as even_file,\
         open(odd_file,"w") as odd_file:
    
       inf=infile.readline()
       num=1
       while(inf):
        print(inf)
        if(num%2==0):
          even_file.write(inf)
        else:
          odd_file.write(inf)
        num +=1
        inf=infile.readline()


input_file = "input_file.txt"
even_file = "even_file.txt"
odd_file = "odd_file.txt"

even_odd_line(input_file,even_file,odd_file)

