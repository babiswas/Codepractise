def min_time_items(arr:list[int],m:int)->int:
    def find_items(arr,mid):
        item=0
        for i in arr:
            item+=mid//i
        return item
    tmax=arr[0]*m
    tmin=1
    while tmin<tmax:
        mid=(tmin+tmax)//2
        num=find_items(arr,mid)
        if num>=m:
            tmax=mid
        else:
            tmin=mid+1
    return tmax
if __name__=="__main__":
    print("Minimum time required to produce m items:")
    arr=[1,2,3]
    tmin=min_time_items(arr,11)
    print(f"Time required to produce 11 items is {tmin}")

        