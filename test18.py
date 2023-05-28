#Median of two sorted array

def find_median_two_sorted(arr1:list[int],arr2:list[int])->int:
        A,B=arr1,arr2
        if len(arr1)>len(arr2):
            A,B=arr2,arr1
        low=0
        high=len(A)
        half=(len(A)+len(B))//2
        total=len(A)+len(B)
        while low<high:
                mid=(low+high)//2
                i=mid
                j=half-mid-2
                A1=A[i] if i>=0 else float("-infinity")
                A2=A[i+1] if i+1<len(A) else float("infinity")
                B1=B[j] if j>=0 else float("-infinity")
                B2=B[j+1] if j+1<len(B) else float("infinity")
                if A1<=B2 and B1<=A2:
                    if total%2!=0:
                          return min(A[i+1],B[j+1])
                    else:
                          return min(A[i+1],B[j+1])+min(A[i],B[j])//2
                elif A1>B2:
                    high=mid-1
                elif B1>A2:
                    low=mid+1
        return -1

if __name__=="__main__":
      print("==================================")
      print("Find the median in two sorted arrays:")
      arr1=[11,14,17,19,21]
      arr2=[10,13,18,20,25,29]
      median_arr=find_median_two_sorted(arr1,arr2)
      test1=sorted(arr1)
      test2=sorted(arr2)
      mid_index=(len(test1)+len(test2))//2
      test1.extend(test2)
      test1=sorted(test1)
      print(f"After extending the array:{test1}")
      print(f"The mid index of the array is {test1[mid_index]}")
      print(f"The median of an array is {median_arr}")
      print("===============================")

                       