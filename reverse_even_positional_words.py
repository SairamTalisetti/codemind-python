s=input()
words=s.split()
for i in range(len(words)):
    if i%2==0:
        print(words[i][::-1],end=" ")
    else:
        print(words[i],end=" ")
        