#Check if array elements are consiquitive

def consiquitive_arr_elements(arr:list[int])->bool:
    temp=min(arr)
    test=0
    for i in range(len(arr)):
        test^=arr[i]^temp
        temp+=1
    if test==0:
        return True
    else:
        return False

if __name__=="__main__":
    print("==================================")
    print(f"Verify if the elements of the array is consiquitive:")
    arr=[2,3,6,7,1,5,4]
    if consiquitive_arr_elements(arr):
        print("The elements of the array is consiquitive")
    else:
        print("The elements of the array is not consiquitive")
    arr=[2,3,7,1,5,4]
    if consiquitive_arr_elements(arr):
        print("The elements of the array is consiquitive")
    else:
        print("The elements of the array is not consiquitive")
    print("=====================================")
