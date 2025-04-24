def count(arr,k,n):
    count=[0]*(k+1)
    b=[0]*n
    for i in range(n):
        count[arr[i]]=count[arr[i]]+1
    for i in range(1,k+1):
        count[i]=count[i-1]+count[i]
    for i in range(n-1,-1,-1):
        count[arr[i]]=count[arr[i]]-1
        b[count[arr[i]]]=arr[i]
    return b
arr=[0,2,5,3,4,4,1,0,8] 
k=max(arr)
n=len(arr)
arr=count(arr,k,n)
arr1=arr.copy()
print("Sorting Array:",arr1)
