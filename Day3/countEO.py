n= int(input("Enter a number: "))

arr=[]
for i in range(n):
    arr.append(int(input("Enter element: ")))

even=0
odd=0

for i in arr:
    if i%2==0:
        even=even+1
    else:
        odd=odd+1


print("Even numbers= ",even)
print("Odd numbers= ",odd)