user_input = input("enter a statement:")
text =user_input.lower()
result = {}
for i in text:
    if i in result:
        result[i]+= 1
    else:
        result[i] =1
print("enter statement:",result)