def searchof(array,search):
    for i in range(0,len(array),1):
        flag=0
        if (array[i]==search):
            print("The element is found in the array")
            flag=0
            break
        else:
            flag=1
    if (flag==1):
        print("The element is not found in the array")
array=list(map(int,input("Enter the array element using space:").split()))
search=int(input("Enter the searching elements:"))
arr1=searchof(array,search)