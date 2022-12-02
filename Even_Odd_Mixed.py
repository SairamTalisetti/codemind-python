n=int(input())
e=[]
o=[]
while n>0:
    r=n%10
    if r%2==0:
        e.append(r)
    else:
        o.append(r)
    n=n//10
if len(e)>0 and len(o)==0:
    print("Even")
elif len(o)>0 and len(e)==0:
    print("Odd")
else:
    print("Mixed")