#problem 1
# a= {
#     "Pankha": "Fan",
#     "Dabba":"Can",
#     "Vastu":"Item"
# }
# print("Options:", tuple(a.keys()))
# b=input("Kripya shabd btaye: ")
# print( "Shabd ka aarth English me hai:",a.get(b))

#problem2
# a1=int(input("Enter Number 1: "))
# a2=int(input("Enter Number 2: "))
# a3=int(input("Enter Number 3: "))
# a4=int(input("Enter Number 4: "))
# a5=int(input("Enter Number 5: "))
# a6=int(input("Enter Number 6: "))
# a7=int(input("Enter Number 7: "))
# a8=int(input("Enter Number 8: "))
# a={a1,a2,a3,a4,a5,a6,a7,a8}
# print("The unique numbers are:\n",a)
# print(type(a))

#problem3
# s={18,"18",18.1,18.0}
# print(s)
#problem4
a1= input( "Friend 1 fav lang: ")
a2= input( "Friend 2 fav lang: ")
a3= input( "Friend 3 fav lang: ")
a4= input( "Friend 4 fav lang: ")
a={}
a["Friend1"]=a1
a["Friend2"]=a2 ##keys have to be unique but values can be same
a["Friend3"]=a3
a["Friend4"]=a4
print(a)