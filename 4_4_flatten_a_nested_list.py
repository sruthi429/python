user_input = eval(input("enter a number:"))
def flatten(nested_list):
    flat = []  
    
    for i in nested_list:
        if type(i) == list:
            flat.extend(flatten(i))
        else:
            flat.append(i)
    
    return flat
print("Flattened list:", flatten(user_input))
