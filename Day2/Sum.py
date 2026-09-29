num=int(input("enter a number: "))
Sum=0
while(num>0):
    Sum += num%10
    num = num//10
print(Sum)    