#Remove an element from an array to make it balanced

def balance_arr(arr:list[int])->int:
    ev_sum=sum([obj for index,obj in enumerate(arr) if index%2==0])
    odd_sum=sum([obj for index,obj in enumerate(arr) if index%2!=0])
    sm_evn=0
    sm_odd=0
    for i in range(len(arr)):
        if i%2==0:
            if ev_sum-sm_evn-arr[i]+sm_odd==odd_sum-sm_odd+sm_evn:
                return i
            sm_evn+=arr[i]
        else:
            if ev_sum-sm_evn+sm_odd==odd_sum-sm_odd-arr[i]+sm_evn:
                return i
            sm_odd+=arr[i]
    return -1

if __name__=="__main__":
    print("==================================")
    print("Find the index which represent equilibrium")
    arr=[5, 5, 2, 5, 8]
    index=balance_arr(arr)
    print(f"The equilibrium index is {index}")
    print("=====================================")
