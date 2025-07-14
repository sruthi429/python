
user_input = int(input("Enter a number: "))
def is_armstrong(user_input):
    number = str(user_input)
    length = len(user_input)
    sum = 0
    for i in user_input:
        sum += int(i) ** length
    return sum == user_input
if is_armstrong(user_input):
    print("It is an Armstrong number:", user_input)
else:
    print("It is not an Armstrong number:", user_input)

   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
'''
    duplicate_input= user_input
    sum=0
    number =len(str(user_input))
    while duplicate_input>0:
        digit=duplicate_input % 10
        sum +=digit**number
        duplicate_input//=10
    return sum==user_input
print(is_amstrong(user_input))
'''