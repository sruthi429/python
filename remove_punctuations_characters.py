import string  
text = input("Enter a sentence with punctuation: ")
no_punctuations= ""
for i in text:
    if i not in string.punctuation:
        no_punctuations.append(i)
print("text without punctuation:", no_punctuations)
