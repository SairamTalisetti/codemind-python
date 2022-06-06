n=int(input())
lst=list(map(int,input().split()))
a=sum(lst)//len(lst)
if a in lst:
    print(True)
else:
    print (False)