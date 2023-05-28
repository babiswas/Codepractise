#Find a pair of numbers with given target
def find_pair(arr:list[int],target:int)->dict[int,int]:
    m=dict()
    for i in range(len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j]==target:
                m.update({arr[i]:arr[j]})
    return m

if __name__=="__main__":
    print("=========================")
    print("Find pairs making a target:")
    arr=[11,21,34,10,32,16,15,19,14,12]
    mp=find_pair(arr,26)
    print(mp)
    print("===============================")
