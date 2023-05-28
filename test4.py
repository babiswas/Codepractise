#Find peak element in an array

def find_peak_element(arr:list[int])->int:

    '''Find peak element in an arrray:'''

    low,high=0,len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if mid>0 and mid<len(arr)-1:
            if arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:
                return mid
            else:
                if arr[mid]<arr[mid-1]:
                    high=mid-1
                else:
                    low=mid+1
        elif mid==0:
            if arr[mid]>arr[mid+1]:
                return mid
            else:
                low=mid+1
        elif mid==len(arr)-1:
            if arr[mid]>arr[mid-1]:
                return mid
            else:
                high=mid-1
    return -1

if __name__=="__main__":
    print("=========================")
    print("Find peak element in an array:")
    arr=[5, 10, 20, 15]
    index=find_peak_element(arr)
    print(f"The peak element is {arr[index]}")
    print("==============================")

