n=input()
a=0
for i in n:
    if ord(i)>a:
        a=ord(i)
        b=i
print(b)