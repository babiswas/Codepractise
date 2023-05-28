def find_min_max_page(arr,K):
    def allocate(arr,mid):
        num_stud=0
        sums=0
        count=0
        for i in range(len(arr)):
            sums+=arr[i]
            if sums>mid:
                count+=1
                sums=arr[i]
        return count+1
    
    pg_max=sum(arr)
    pg_min=max(arr)
    while pg_min<pg_max:
        mid=(pg_max+pg_min)//2
        num_stud=allocate(arr,mid)
        if num_stud==K:
            pg_max=mid
        if num_stud>K:
            pg_min=mid+1
        elif num_stud<K:
            pg_max=mid-1
    return pg_max

if __name__=="__main__":
    print("=============================")
    print("Find the minimum of the maximum page that can be allocated:")
    arr=[12, 34, 67, 90]
    pages=find_min_max_page(arr,2)
    print(f"The minim of the max pages is {pages}")
    print("================================")
