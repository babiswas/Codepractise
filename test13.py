#Minimum jumps to the end of an array
import sys
def find_min_jumps(arr):
    steps=arr[0]
    count=0
    maxm=-sys.maxsize+1
    for i in range(1,len(arr)-1):
        steps-=1
        if maxm<arr[i]+i:
            maxm=arr[i]+i
        if steps==0:
            steps=maxm-i
            count+=1
    return count+1

if __name__=="__main__":
    print("========================")
    print("The minimum jumps to the end of array is:")
    arr=[1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
    index=find_min_jumps(arr)
    print(f"Minimum jumps required is {index}")
    print("==========================")
