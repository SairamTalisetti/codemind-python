n=int(input())
s=0
lst=list(map(int,input().split()))
for i in range(1,n-1):
    if lst[i]%2==1 and lst[i-1]%2==1 and lst[i+1]%2==1:
        s=s+1
print(s)