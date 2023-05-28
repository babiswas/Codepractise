def insertion_sort(arr:list[int])->None:
    index=1
    while index<len(arr):
        element=arr[index]
        hole=index
        while element<arr[hole-1]:
            arr[hole]=arr[hole-1]
            hole=hole-1
            if hole<=0:
               break
        arr[hole]=element
        index+=1
if __name__=="__main__":
    print("===========================")
    print("The insertion sort of the array is:")
    arr=[12,10,9,13,10,6,14,4,5]
    insertion_sort(arr)
    print(arr)
    print("==============================")

            