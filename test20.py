#Quick select algorithm
#Third largest number

def partition(arr:list[int],start:int,end:int)->int:
    index=start-1
    pivot=arr[end]
    for i in range(start,len(arr)):
        if arr[i]<pivot:
            index+=1
            arr[index],arr[i]=arr[i],arr[index]
    index+=1
    arr[index],arr[end]=pivot,arr[index]
    return index

def quick_select_algorithm(arr:list[int],start:int,end:int,index:int)->int:
    if start<=end:
        num=partition(arr,start,end)
        if num==index-1:
            return arr[num]
        num1=quick_select_algorithm(arr,start,num-1,index)
        num2=quick_select_algorithm(arr,num+1,end,index)
        if num1==-1:
            return num2
        elif num2==-1:
            return num1
    else:
        return -1

if __name__=="__main__":
    print("=========================")
    arr=[11,10,23,4,56,25,19,34,12]
    print("Third smallest number")
    num=quick_select_algorithm(arr,0,len(arr)-1,3)
    print(arr)
    print(f"The third smallest number is {num}")
    print("==============================")