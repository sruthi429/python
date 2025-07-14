m = int(input("enter a number"))
def sumofdigits(m):
    sum=0
    while m>0:
        digit = m % 10
        sum+=digit   
        m//=10
    return sum
print(sumofdigits(m))