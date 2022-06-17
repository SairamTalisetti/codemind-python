n=input()
words=n.split()
lengts=[len(i) for i in words]
print(min(lengts))