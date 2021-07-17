x = input("enter numbers with space\n").split()
a=0
p=input("enter searching No\n")
for i in range (len(x)):
    if x[i]==p:
        a+=1

if a==1:
    print("\npresent")
else:
    print("\nnot present")
