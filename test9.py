#Find second largets element in an array

def find_second_largest(arr:list[int])->int:
    large2=arr[0]
    large1=arr[0]
    for i in range(1,len(arr)):
        if arr[i]>large1:
            large2,large1=large1,arr[i]
        elif large2<arr[i]:
            large2=arr[i]
    return large2

if __name__=="__main__":
    print("===============================")
    print("Find the second largets element in an array:")
    arr=[12,17,9,16,11,21,45,13]
    num=find_second_largest(arr)
    print(f"The second largets element in an array is {num}")
    print(sorted(arr))
    print("====================================")


