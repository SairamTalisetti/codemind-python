x,y=map(int,input().split())
for i in range(1,y+1):
    if (y*i)%x==0:
        print(y*i)
        break