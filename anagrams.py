word1 = input("Enter first string: ")
word2 = input("Enter second string: ")
def is_anagram(str1, str2):
    str1 = str1.replace(" "," ")
    str2 = str2.replace(" "," ")
    return sorted(str1) == sorted(str2)
if is_anagram(word1, word2):
    print("The strings are anagrams.")
else:
    print("The strings are NOT anagrams.")
