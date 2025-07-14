user_input = list(map(int,input("enetr a list").split(",")))
def bubblesort(user_input):
    for i in range(len(user_input)-1):
        for j in range(len(user_input)-1-i):
            if user_input[j]>user_input[j+1]:
                user_input[j]+=user_input[j+1]
                user_input[j+1]=user_input[j]-user_input[j+1]
                user_input[j]-=user_input[j+1]
    return user_input        
print(bubblesort(user_input))
