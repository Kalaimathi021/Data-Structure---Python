def sortedlist(arr):
   for i in range(0,len(arr)-1):
      min_i=i
      for j in range(i+1,len(arr)):
         if arr[j]<arr[min_i]:
            min_i=j
      temp=arr[i]
      arr[i]=arr[min_i]
      arr[min_i]=temp
arr=[8,6,2,5,4,9,11]
sortedlist(arr)
print("Sorted array list:",arr)

