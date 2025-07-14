user_input = list(map(int,input("enter a numbers").split(",")))
target = int(input("enter a number to search"))

#print (linear_search(user_input,target))
def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

print (linear_search(user_input,target))