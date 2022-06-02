def ad(n):
    co=0
    while n>0:
        a=n%10
        n=n//10
        co=co+a
    return co
  
a=int(input())
while a>9:
    a=ad(a)
print(a)

  