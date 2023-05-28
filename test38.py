#Minimum operations to switch on all bulbs

def min_ops(arr:list[int]):
    count=0
    for i in range(len(arr)):
        if count%2!=0:
            arr[i]=not arr[i]
        if arr[i]==0:
            count+=1
    return count


if __name__=="__main__":
    print("===========================")
    print("Minimum number of operation to switch on all lights:")
    arr=[1,0,0,0,0]
    num=min_ops(arr)
    print(f"The minimum number of operation is {num}")
    print("=================================================")