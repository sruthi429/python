list1 = list(map(int, input("Enter the first list: ").split()))
list2 = list(map(int, input("Enter the second list: ").split()))
common_elements = []
for i in list1:
    if i in list2 and i not in common_elements:
        common_elements.append(i)
print("Common elements:", common_elements)
