pos = -1

def search(list , n):
    l=0
    u=len(list)-1
    while l<= u:
        mid = (l+u)//2

        if list[mid]==n:
            globals()['pos']=mid
            return True
        else:
            if list[mid]<n:
                l=mid+1
            else:
                u=mid-1
    return False


list = [5,4,6,7,9,18,45]

n = int ( input("Enter value to search"))

if search(list,n):
    print("found at position", pos+1)
else:
    print("not found")