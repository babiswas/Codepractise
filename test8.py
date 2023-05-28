#Find the number of subsets with product less than 

def find_subset(arr,n,K,mul):
    if n==0:
        return 0
    elif mul>K:
        return 0
    else:
        if n-1>=0 and mul*arr[n-1]<=K:
            return 1+find_subset(arr,n-1,K,mul*arr[n-1])+find_subset(arr,n-1,K,mul)
        else:
            return find_subset(arr,n-1,K,mul)
        

if __name__=="__main__":
    print("===================================")
    print("Find the number of subset with result less than K")
    arr=[2, 4, 5, 3]
    num=find_subset(arr,len(arr),12,1)
    print(f"The number of subset with result less than k is {num}")
    print("======================================")
        
