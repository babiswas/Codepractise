import sys
def find_all_platforms(arr1:list[int],arr2:list[int])->int:
    maxm=-sys.maxsize+1
    counter=0
    arr1.sort()
    arr2.sort()
    index=0
    for i in range(len(arr1)):
        if arr2[index]>arr1[i]:
            counter+=1
            if maxm<counter:
                maxm=counter
        else:
            while arr2[index]<arr1[i]:
                index+=1
                counter-=1
            counter+=1
    return maxm

if __name__=="__main__":
    print("========================")
    print("The maximum number of platforms is:")
    arr1=[900,940,950,1100,1500,1800]
    arr2=[910,1200,1120,1130,1900,2000]
    platforms=find_all_platforms(arr1,arr2)
    print(f"The minimum number of platforms is {platforms}")
    print("=================================")

