a=int(input("Enter the Number: "))
b=int(input("Enter the Number: "))
while(b!=0):
    temp=b
    b=a%b
    a=temp
print(a)    