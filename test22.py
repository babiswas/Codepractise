#Find missing number in an array

def find_missing_num(arr:list[int],n:int):
    sn=(n*(n+1))//2
    sm=0
    for i in arr:
        sm+=i
    return sn-sm

if __name__=="__main__":
    print("=========================")
    arr=[1,2,3,4,5,7,8,9]
    print("The missing number is:")
    print(find_missing_num(arr,9))
    print("============================")

