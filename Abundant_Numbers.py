x=int(input())
fc=0
for i in range(1,x):
    if x%i==0:
        fc+=i
print(fc>x)