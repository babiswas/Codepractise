#Find minimum difference between a pair of elements
import sys

def find_minm_diff(arr:list[int])->int:
    arr.sort()
    print(arr)
    diff=sys.maxsize-1
    for i in range(len(arr)-1):
        if diff>arr[i+1]-arr[i]:
            diff=arr[i+1]-arr[i]
    return diff

if __name__=="__main__":
    print("==========================")
    arr=[12,10,17,15,19,21,24,28,26]
    diff=find_minm_diff(arr)
    print(f"The minimum difference is {diff}")
    print("===============================")


