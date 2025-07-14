myList = list(map(int,input("enter a numbers").split(",")))
evensum=0
oddSum=0
for i in myList:  
    if(i%2==0):
        evensum+=i
    else:
        oddSum+=i
print(evensum)
print(oddSum)