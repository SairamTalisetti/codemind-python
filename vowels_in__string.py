s=input()
visited=[]
vowels="aeiouAEIOU"
for i in s:
    if i in vowels and i not in visited:
        print(i,end=" ")
        visited.append(i)