import math

def jump(array,search):
    step = math.sqrt(len(array))
    prev =0
    while(array[int(min( step, len(array)) -1 )] < search ):
        prev = step
        step += math.sqrt(len(array))
        if prev >= len(array):
            return -1
    while array[int(prev)] < search:
        prev += 1
        if prev == min(step, len(array)):
            return -1
    if array[int(prev)] == search:
        return prev
    
    return -1

#driver code

for i in range(int(input())):
    # array = input().split()
    array = list(map(int, input().split()))
    search = int(input())

    res = jump(array,search)
    res = int(res)
    if res == -1:
        print("number is not present in array ")
    else:
        print("Number is present at Index :",res+1)