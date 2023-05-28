def find_pair(arr:list[int],target)->tuple[int,int]:
    arr.sort()
    index1=0
    index2=len(arr)-1
    while index1<=index2:
        num=target-arr[index1]
        if num==arr[index2]:
            return arr[index1],arr[index2]
        elif num>arr[index2]:
            index1+=1
        elif num<arr[index2]:
            index2-=1
    return -1,-1
if __name__=="__main__":
    print("==============================")
    print("Find a pair of elements making a target:")
    arr=[11,10,14,16,19,21,4,8,12]
    num1,num2=find_pair(arr,26)
    print(num1,num2,"is the pair of numbers")
    print("====================================")
