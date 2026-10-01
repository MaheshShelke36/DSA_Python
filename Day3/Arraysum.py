#calculate Array sum

n=int(input("Enter a number of elements: "))
arr=[]

for i in range(n):
    x=int(input("Enter elements "))
    arr.append(x)

sum=0

for i in arr:
    sum = sum+i
print("sum = ",sum)  