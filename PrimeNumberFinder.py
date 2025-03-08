n= int(input("Enter Your Number please : "))

for i in range(2,n):
    if(n%i ) ==0:
        print("Number not a Prime number ")
        break

else:
    print("Number is prime")
