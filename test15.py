def partition(arr:list[int],start:int,end:int)->int:
    index=start-1
    pivot=arr[end]
    for i in range(start,len(arr)):
        if arr[i]<pivot:
            index+=1
            arr[index],arr[i]=arr[i],arr[index]
    index+=1
    arr[index],arr[end]=arr[end],arr[index]
    return index

def qsort(arr:list[int],start:int,end:int)->None:
    if start<=end:
        index=partition(arr,start,end)
        qsort(arr,start,index-1)
        qsort(arr,index+1,end)

if __name__=="__main__":
    print("=================================")
    print("Quick sort algorithm")
    arr=[11,10,9,18,6,12,5,3,15]
    qsort(arr,0,len(arr)-1)
    print(arr)
    print("==============================")

