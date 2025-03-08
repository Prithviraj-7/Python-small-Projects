m1= int(input("Enter Your Marks of English "))    
m2= int(input("Enter Your Marks of Maths "))
m3= int(input("Enter Your Marks of Science ")),                 """Change Subject accordingly also change no. of subjects as per your choice"""
m4= int(input("Enter Your Marks of Social Studies "))
m5= int(input("Enter Your Marks of Secondary language "))
m6= int(input("Enter Your Marks of IT "))

tp=round((100*(m1+m2+m3+m4+m5+m6)/600), 2)    #tp = Total percentage

if(tp>=40):
    print("YOUR HAVE PASSED THE EXAM!""\n" "PERCENTAGE =", tp,"%") # My minimum percentage for passing is 40% change accordingly 

else:
    print("YOUR ARE FAILED, try next year""\n" "PERCENTAGE=", tp,"%")    


if(tp<=100 and tp>=90 ):
    print("Grades:- Ex")    #Ex= Excellent

elif(tp<=90 and tp>=80): 
    print("Grades:- A")
elif(tp<=80 and tp>=70): 
    print("Grades:- B")
elif(tp<=70 and tp>=60): 
    print("Grades:- C")
elif(tp<=60 and tp>=50): 
    print("Grades:- D")
elif(tp<50):
    print("Grades:- F") 
