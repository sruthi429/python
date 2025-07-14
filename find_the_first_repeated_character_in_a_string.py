def repeated(str):
    visited={}
    for i in str:
        if visited.get(i):
            return i
        else:
            visited[i]=True
txt = "abcba"
print(repeated(txt))


