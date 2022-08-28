#pr1
# print("Warning! You cannot enter same numbers.")
# a1=int(input("Enter no. 1: "))
# a2=int(input("Enter no. 2: "))
# a3=int(input("Enter no. 3: "))
# a4=int(input("Enter no. 4: "))
# if(a1>a2 and a3>a4):
#     if(a1>a3):
#         print("Greatest no. is", a1)
#     else:
#         print("Greatest no. is", a3)
# if(a2>a3):
#         print("Greatest no. is", a2)
# elif(a3>a2):
#         print("Greatest no. is", a3)
# elif(a2>a4):
#     print("Greatest no. is", a2)
# else:
#     print("Greatest no. is", a4)

#pr2
# b1=int(input("Enter the total marks of subject1: "))
# b2=int(input("Enter the total marks of subject2: "))
# b3=int(input("Enter the total marks of subject3: "))
# a1=int(input("Enter the marks obtained in Subject1: "))
# a2=int(input("Enter the marks obtained in Subject2: "))
# a3=int(input("Enter the marks obtained in Subject3: "))
# c=(b1+b2+b3)/3
# b= (a1+a2+a3)/3
# if(a1>= 0.33*b1 and a2>= 0.33*b2 and a3>= 0.33*b3):
#     if(b>=0.40*c):
#         print("PASS")
#     else:
#         print("Fail due to less Total marks")
# else:
#     print("Fail due to less Subject marks")

#pr3
a=input("Enter your message:\n")
if("make a lot of money" in a or "buy now" in a or"suscribe this" in a or"click this" in a):
    print("Spam Message")
else:
    print("Genuine message")

#pr5
# a=input("Username: ")
# if(len(a)<10):
#     print("The user name has less than 10 characters")
# else:
#     print("The user name has more than or equal to 10 characters")

#pr5
# a=["Ankit","Ketan","Akanksha","Cherry"]
# b=input("enter the name: ")
# if(b in a):
#     print("The name is prestent in the list")
# else:
#     print("The name is not prestent in the list")

#pr6
# a=int(input("Enter your total obtained marks: "))
# if(a>90 and a<=100):
#     print("Ex")
# elif(a>80 and a<=90):
#     print("A")
# elif(a>70 and a<=80):
#     print("B")
# elif(a>60 and a<=700):
#     print("C")
# elif(a>50 and a<=60):
#     print("D")
# else:
#     print("F")