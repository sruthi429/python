s = {'sruthi':4,'raaaam':5 }
vowels = 'aeiou'
result = []
frequency=[]
for k in s.keys():
    for c in k:
        if c in vowels:
            if c in result:
                i=result.index(c)
                count=frequency[i]
                count+=1
                frequency[i]=count 
            else:      
                result.append(c)
                frequency.append(1)
print("vowels:",result)
print("frequencies",frequency)