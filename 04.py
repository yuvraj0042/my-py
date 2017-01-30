a=input("entre the no")
if a>1:
    for i in range(2,a):
        if (a%i)==0:
            print("no is not prime")
            break
    else:
        print("no is prime")
else:
    print(a,"not a prime no")









    
