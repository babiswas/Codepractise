def rotate_array(arr,target):
    low,high=0,len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]>arr[low]:
            if target<arr[mid] and target>=arr[low]:
                high=mid-1
            else:
                low=mid+1
        else:
            if target>arr[mid] and target<=arr[high]:
                low=mid+1
            else:
                high=mid-1
    return -1

if __name__=="__main__":
    print("======================")
    print("Find target in rotated array:")
    arr=[6,7,8,9,10,1,2,3,4,5]
    for i in arr:
        index=rotate_array(arr,i)
        print(f"The desired index is {index}")
    print("===============================")
            
