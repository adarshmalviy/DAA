def search(x, s , l ,r):
    while l<=r:
        mid =  l+r//2
        if x[mid] == s:
            return mid;
        elif x[mid]>s:
            l = mid + 1
        else:
            r = mid -1

    return -1

for i in range(int(input())):
    # n = int(input("enter n"))
    x = input("enter numbers with space\n").split()
    s = input("enter number to search")
    res = search(x, s, 0, len(x)-1)

    if res!=-1:
        print("number is present at index " , res+1)
    else:
        print("number is not present ")

