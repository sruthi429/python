user_input = list(map(int,input("enter a numbers").split(",")))
temp = []
for i in user_input:
    if i not in temp:
        temp.append(i)

print(temp)
