user_input = input("enter a sentence:")
word_list = user_input.split()
def find_longest_word(word):
    longest=" "
    for i in word:
        if len(i) > len(longest):
            longest = i
    return longest
print("enter a sentence:",find_longest_word(word_list))