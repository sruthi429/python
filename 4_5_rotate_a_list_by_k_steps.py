user_input = list(map(int,input("enter a list:").split(",")))
steps = int(input("Enter number of steps to rotate: "))
def rotate_list(lst, k):
    n = len(lst)
    k = k % n  
    return lst[-k:] + lst[:-k]
rotated = rotate_list(user_input, steps)
print("Rotated list:", rotated)
