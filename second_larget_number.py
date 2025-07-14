myList = list(map(int,input("enter a numbers").split(",")))
for i in range(0,2):
    for j in range(len(myList)-1-i):
        if(myList[j]>myList[j+1]):
            myList[j]+=myList[j+1]
            myList[j+1]=myList[j]-myList[j+1]
            myList[j]-=myList[j+1]
print(f"My second largest number in the list is: {myList[len(myList)-2]}")