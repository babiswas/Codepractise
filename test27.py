def find_minm(arr:list[int])->int:
    low,high=0,len(arr)-1
    while low<=high:
        if arr[low]<arr[high]:
            return arr[low]
        mid=(low+high)//2
        if arr[mid]>arr[mid+1]:
            return mid+1
        elif arr[mid]<arr[mid-1]:
            return mid
        if arr[mid]>arr[low]:
            low=mid+1
        else:
            high=mid-1
    return -1

if __name__=="__main__":
    print("====================================")
    print("Find minimum number in a rotated array")
    arr=[14,15,16,10,11,12,13]
    num=find_minm(arr)
    print(f"The minimum number in the array is {arr[num]}")
    print("=====================================")
