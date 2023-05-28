#Kth smallest absolute difference

def kth_smallest(arr,K):
    def find_ksmall(arr,mid):
        count=0
        index1=0
        index2=1
        while index1<len(arr) and index2<len(arr) and index1<=index2:
                if arr[index2]-arr[index1]<=mid:
                    count+=index2-index1
                elif arr[index2]-arr[index1]>mid:
                        while arr[index2]-arr[index1]>mid:
                            index1+=1
                            count+=index2-index1
                index2+=1
        return count
                
    arr.sort()
    max_diff=max(arr)-min(arr)
    min_diff=9999999
    for i in range(1,len(arr)):
        if min_diff>arr[i]-arr[i-1]:
            min_diff=arr[i]-arr[i-1]
    while min_diff<max_diff:
        mid=(min_diff+max_diff)/2
        num=find_ksmall(arr,mid)
        if num>=K:
             max_diff=mid 
        elif num<K:
             min_diff=mid+1
    return max_diff

if __name__=="__main__":
    print("=============================")
    arr=[1,2,3,4]
    index=kth_smallest(arr,3)
    print(f"The {index} is the mid 3rd smallest diffence")
    print("=============================")
     


