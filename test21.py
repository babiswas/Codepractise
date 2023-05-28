#Triplets in an array

def find_triplets(arr:list[int]):
    counter=0
    for i in range(len(arr)-2):
        for j in range(i+1,len(arr)-1):
            for k in range(j+1,len(arr)):
                if (arr[i]+arr[j]==arr[k]) or (arr[i]+arr[k]==arr[j]) or (arr[j]+arr[k]==arr[i]):
                    print(f"The triplets is {arr[i]},{arr[j]},{arr[k]}")
                    counter+=1
    print(f"The number of triplets are {counter}")

def find_triplets_better_version(arr:list[int]):
    buffer=[0]*1000
    for i in arr:
        buffer[i]=1
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if buffer[arr[i]+arr[j]]==1:
                print(f"The triplets is {arr[i]},{arr[j]},{arr[i]+arr[j]}")

if __name__=="__main__":
    print("==========================")
    print(f"Find triplets in an array:")
    arr=[12,11,18,21,23,14,19,7]
    find_triplets(arr)
    print(f"Triplets better version implementation:")
    find_triplets_better_version(arr)
    print("==============================")