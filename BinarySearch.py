#completed
def binarysearch(array,search,low,high):
    while low<=high:
        mid=low+(low-high)//2
        if array[mid]==search:
            return mid
        elif array[mid]<search:
           low=mid+1
        elif array[mid]>search:
            high=mid-1

    return -1
array=[]
num=int(input("Enter the number of array elements:"))
for i in range(0,num):
    element=int(input("Enter the array elements:"))
    array.append(element)
search=int(input("Enter the elements to find:"))
result=binarysearch(array,search,0,len(array)-1)
if result!=-1:
    print("The element is found at the index:",i-1)
else:
    print("The element is not found")