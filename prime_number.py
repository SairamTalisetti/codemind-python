x=int(input())
fc=0
for i in range(1,x+1):
    if x%i==0:
        fc+=1
if fc==2:
    print("prime")
else:
    print("not a prime")