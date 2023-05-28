def bubble_sort(arr:list[int])->None:
    index=len(arr)-1
    while index>=0:
        for i in range(index):
            if arr[i]>arr[i+1]:
                arr[i+1],arr[i]=arr[i],arr[i+1]
        index-=1
if __name__=="__main__":
    print("===========================")
    print("Bubble sort algorithm")
    arr=[11,12,10,9,4,3,14,16,1]
    bubble_sort(arr)
    print(arr)
    print("==============================")
