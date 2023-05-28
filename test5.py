#Kadanes algorithm
import sys
def kadanes_algo(arr:list[int])->int:
    sm=0
    maxm=-sys.maxsize+1
    first_index=0
    last_index=0
    index1=0
    for i in range(len(arr)):
        sm+=arr[i]
        if sm>maxm:
            maxm=sm
            first_index=index1
            last_index=i
        if sm<0:
            sm=0
            index1=i+1
            if i+1>=len(arr):
                break
    return maxm,first_index,last_index

if __name__=="__main__":
    print("=======================")
    print("Kadanes Algorithm:")
    arr=[-2,-3,4,-1,-2,1,5,-3]
    max_sum,index1,index2=kadanes_algo(arr)
    print(f"The maximum sum is {max_sum}")
    print(f"The max sum array is {arr[index1:index2+1]}")
    print("===============================")
