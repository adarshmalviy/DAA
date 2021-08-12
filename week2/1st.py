
# Function to find the first occurrence of a given number
# in a sorted list of integers
def findFirstOccurrence(A, x):
 
    (left, right) = (0, len(A) - 1)
 
    result = -1
 
    while left <= right:
 
        # find the mid-value in the search space and compares it with the target
        mid = (left + right) // 2
 
        # if the key is located, update the result and
        # search towards the left (lower indices)
        if x == A[mid]:
            result = mid
            right = mid - 1
 
        # if the key is less than the middle element, discard the right half
        elif x < A[mid]:
            right = mid - 1
 
        # if the key is more than the middle element, discard the left half
        else:
            left = mid + 1
 
    # return the leftmost index, or -1 if the element is not found
    return result

# Function to find the last occurrence of a given number
# in a sorted list of integers
def findLastOccurrence(A, x):
 
    # search space is `A[left…right]`
    (left, right) = (0, len(A) - 1)
 
    # initialize the result by -1
    result = -1
 
    # loop till the search space is exhausted
    while left <= right:
 
        # find the mid-value in the search space and compares it with the target
        mid = (left + right) // 2
 
        # if the key is located, update the result and
        # search towards the right (higher indices)
        if x == A[mid]:
            result = mid
            left = mid + 1
 
        # if the key is less than the middle element, discard the right half
        elif x < A[mid]:
            right = mid - 1
 
        # if the key is more than the middle element, discard the left half
        else:
            left = mid + 1
 
    # return the leftmost index, or -1 if the element is not found
    return result

for i in range(int(input())):
    _ = int(input())
    array = list(map(int, input().split()))
    find = int(input())
    # result  = search(array,find,0,len(array)-1)
    f1 = findFirstOccurrence(array, find)
    f2 = findLastOccurrence(array, find)
    print(f2-f1+1)

