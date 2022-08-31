x,y=map(int,input().split())
l=[]
for i in range(1,y+1):
    if x%i==0 and y%i==0:
        l.append(i)
print(max(l))