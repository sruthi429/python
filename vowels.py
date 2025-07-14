user_input = input("enter a string:")
vowels = {'a':0,'e':0,'i':0,'o,':0,'u':0}
user_input=user_input.lower()
for char in user_input:
    if char in vowels:
        vowels[char]+=1
print(vowels)




