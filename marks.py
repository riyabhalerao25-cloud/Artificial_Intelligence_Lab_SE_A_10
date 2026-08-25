r=int(input("enter marks of maths: "))
a=int(input("enter marks of english: "))
b=int(input("enter marks of physics: "))
c=int(input("enter marks of chemistry: "))
d=int(input("enter marks of biology: "))
t=int(input("enter total marks: "))
total=a+b+c+d+r
percent=((total/t)*100)
print("percentage = ",percent)
if(percent<= 40):
     print("fail")
elif(percent<65):
     print("II class")
elif(percent<75):
     print("I class")
else:
     print("distinction")
