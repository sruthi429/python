original_list = list(map(int,input("enter a numbers").split(",")))
n = len(original_list)
for i in range(n // 2):
    temp = original_list[i]
    original_list[i] = original_list[n - 1 - i]
    original_list[n - 1 - i] = temp
print("Reversed list:", original_list)
