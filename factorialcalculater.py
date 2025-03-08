# n=int(input("Enter your no. :"))

# i=1                      
# product=1                                   
# while(i<=n ):                
#     product *= i
#     i += 1


# # product=1 
# # for i in range(1,n+1 ): 
# #     product= product*i

"""There is one catch ie code mention above not valid for n=0"""

# print (product ,f"is Factorial of {n}")    



# NEW WAY 

def factorial(n):
    if(n==1 or n==0):
        return 1 
    return n* factorial(n-1)
n=int(input("Enter YOur Number Please :"))

print (f"Factorial of {n} :", factorial(n)),

"""  Here now 0!=1 is showing  """
    
