#Rotate an array efficiently

def rotate(arr,k):
    def reverse_arr(arr,index1,index2):
        while index1<index2:
            arr[index1],arr[index2]=arr[index2],arr[index1]
            index1+=1
            index2-=1
    reverse_arr(arr,len(arr)-1-k+1,len(arr)-1)
    reverse_arr(arr,0,len(arr)-1-k)
    reverse_arr(arr,0,len(arr)-1)
    return arr

if __name__=="__main__":
    print("============================")
    print("Rotating an array")
    arr=[1,2,3,4,5,6,7]
    rotate(arr,3)
    print(arr)
    print("=================================")
    