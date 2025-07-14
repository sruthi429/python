a = int(input("Enter start range: "))
b = int(input("Enter end range: "))
for num in range(a, b + 1):
    isprime = True
    for i in range(2, num//2+1):
        if num % i == 0:
            isprime =False
            break  
    if isprime==True and num>1:
        print(num, end=' ')

