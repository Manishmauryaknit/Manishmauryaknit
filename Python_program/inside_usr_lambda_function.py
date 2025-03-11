#!/usr/bin/python3.12

print("***inside userdefined function lambda function with defferent function**\n")

table=lambda x:[print(i) for i in range(x)]
sqr=lambda x:[print(f"sqr of {i}=:{i*i}") for i in range(x)]
sqr_root=lambda x:[print(f"sqr_root of {i}:{i**(1/2)}") for i in range(x+1)]
even=lambda x:[(print("odd",i)if i%2 else print("even",i)) for i in range(1,x)]

x=int(input("enter number"))
print("operation:","table","sqr","sqr_root","even")
opra=str(input("enter operation:"))
def op(x,*opra):
    
    match opra:
        case ope if "table" in ope:
            print("table of given number range")
            c=table(x)
            
        case ope if "sqr" in ope:
            print("square of given number range ")
            c=sqr(x)
        case ope if "sqr_root" in ope:
            print("sqr_root of given number range")
            c=sqr_root(x)
            #print(c)  
        case ope if "even" in ope:
            print("finidng even odd number")
            c=even(x)
        case _:
            print("table of given number range")
            table(x)
            print("square of given number range ")
            sqr(x)
            print("sqr_root of given number range")
            sqr_root(x)
            print("finidng even odd number")
            even(x)
            

op(x,opra)  
