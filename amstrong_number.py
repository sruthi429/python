user_input = int(input("Enter a number: "))

def is_armstrong(user_input):
    number = str(user_input)
    length = len(number)
    total = 0
    for i in number:
        total += int(i) ** length
    return total == user_input

if is_armstrong(user_input):
    print("It is an Armstrong number:", user_input)
else:
    print("It is not an Armstrong number:", user_input)

   
   
   
   
   
   
   
   