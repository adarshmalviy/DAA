for j in range(int(input())):
    _ = int(input("enter n"))
    x = input("enter numbers with space\n").split()
    a=0
    p=input("enter searching No\n")
    for i in range (len(x)):
        if x[i]==p:
            a+=1
            t = i
    if a==1:
        print("\npresent",t+1)
    else:
        print("\nnot present",i+1)
