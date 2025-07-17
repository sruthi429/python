user_input = input("enter a semtence:")
def capatilize_word(text):
 result ="" 
 for i in text.split(" "): 
  result += i[0].upper() + i[1:] +' '
 return result
print(capatilize_word(user_input))