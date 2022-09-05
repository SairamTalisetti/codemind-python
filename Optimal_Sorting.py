t=int(input())
for tu in range(t):
    x=int(input())
    l=[int(i)for i in input().split()]
    l1=sorted(l)
    if l==l1:
        print(0)
    else:
        print(max(l1)-min(l1))