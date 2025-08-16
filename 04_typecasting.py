a="39.2" 
print(type(a)) #class <string>
a=float(a) #type casting str into float
print(type(a)) #class <float>
a=input("Enter number 1")  #take number as string
b=input("Enter number 2")
print(a+b) #concadinate two string

#We need to typecast the input to basis of need other wise it will take value as string
a= int(input("Enter a number"))
b= int(input("Enter a 2nd number"))
print("Sum is " a+b)
