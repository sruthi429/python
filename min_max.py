user_input =list(map(int,input("enter a values:").split(",")))
def max_min(a):
    max_val = a[0]
    min_val = a[0]
    
    for i in a:
        print(i,min_val)
        if i > max_val:
            max_val = i
        if i < min_val:
            min_val = i
    
    print("min:", min_val)
    print("max:", max_val)

max_min(user_input)