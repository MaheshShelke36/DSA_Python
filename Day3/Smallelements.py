#smallest, largest,second smallest and second largest number
n= int(input("enter numbers: "))
arr=[]

for i in range(3):
    arr.append(int(input("Enter elements: ")))

arr.sort()

print("Smallest: ", arr[0])
print("second Smallest: ", arr[1])
print("Largest: ",arr[-2])
print("second Largest: ",arr[-1])