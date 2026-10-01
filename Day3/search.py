n= int(input("Enter number of elements: "))
arr=[]

for i in range(n):
    arr.append(int(input("Enter Elements: ")))

x=int(input("Enter number to search: "))
found=False

for i in range(n):
    if arr[i]==x:
        print("Element found at position",i+1)
        found=True
        break

if found==False:
    print("Element not found")    
