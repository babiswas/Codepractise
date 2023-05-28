def partition(arr:list[int],start:int,end:int)->int:
    index=start-1
    pivot=arr[end]
    for i in range(index,len(arr)):
        if arr[i]<pivot:
            index+=1
            arr[index],arr[i]=arr[i],arr[index]
    index+=1
    arr[index],arr[end]=pivot,arr[index]
    return index

if __name__=="__main__":
    print("=================================")
    print("Partition an array:")
    arr=[11,10,9,15,14,4,8,0,12]
    index=partition(arr,0,len(arr)-1)
    print(index)
    print(arr)
    print("===============================")
