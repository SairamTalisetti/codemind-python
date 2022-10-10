n=int(input())
l=[i for i in str(n)]
for i in range(len(l)):
    if l[i]=="6":
        l[i]="9"
        break
print("".join(l))
        