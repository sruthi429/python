sentence = input("enetr a sentence:")
sentence = sentence.lower()
alphabets = []
for i in sentence:
    if i >= 'a' and i <= 'z' and i not in alphabets:
        alphabets.append(i)
if len(alphabets) == 26:
    print("This is a pangram.")
else:
    print("This is not a pangram.")

