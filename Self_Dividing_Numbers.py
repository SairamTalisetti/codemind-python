n=int(input())
m=int(input())
for i in range(n,m+1):  
    d=i     
    c=1
    while i>0:
        r=i%10
        if r!=0:
            if d%r!=0:
                c=0
        if r==0:
            c=0
        i=i//10
    if c==1:
        print(d,end=" ")