def hashfunction(data, size):
    u = (2*data+3)%size
    return u
def linear_probing(u, i, size):
    return (u+i)%size

def main():
    size = int(input("Enter the size of the array: "))
    Hashtable = [-1] * size 
    for i in range(size):
        data = int(input("Enter the data (or) value: "))
        u = hashfunction(data, size)  
        i = 0
        while Hashtable[u] != -1:
            u = linear_probing(u,i,size)  
            i += 1
        Hashtable[u] = data
    print(Hashtable)

if __name__ == "main":
    main()
