#K frequent numbers
import heapq
import sys

def find_k_frequent_numbers(arr:list[int],K:int)->dict[int,int]:
    l=list()
    heapq.heapify(l)
    m=dict()
    answer=dict()
    for i in arr:
        count=m.get(i,0)
        m.update({i:count+1})
    for key,value in m.items():
        heapq.heappush(l,(-value,key))
    while K>0:
        item=heapq.heappop(l)
        answer.update({item[1]:-1*item[0]})
        K-=1
    return answer

if __name__=="__main__":
    print("===============================")
    print("Find k frequent numbers:")
    arr=[12,11,13,12,15,16,14,17,18,13,12,15,10,16,19,20,21,13,14,16,8]
    answer=find_k_frequent_numbers(arr,5)
    print(answer)
    print("===========================================")

    
