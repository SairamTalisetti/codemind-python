x=int(input())
l=[int(i) for i in input().split()]
e=0
for i in l:
    if i==0:
        e+=1
        l.remove(i)
        l.insert(x-1,0)
print(*l)