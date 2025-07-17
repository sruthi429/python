#Find the First Non-Repeating Character in a String
character = input("enter a string:")
def first_non_repeating(c):
    for i in c:
        if c.count(i)==1:
            return i
        else:
            return None
print(first_non_repeating(character))