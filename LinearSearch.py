pos = -1
def search(list,n):
    i = 0
    while i<len(list):
        if list[i]==n:
            globals()['pos'] = i
            return True
        i +=1
    return False

list = [5,6,4,7,2,18,45]

n = int ( input("Enter value to search"))

if search(list,n):
    print("found at position", pos+1)
else:
    print("not found")