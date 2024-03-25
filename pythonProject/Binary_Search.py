pos = -1      # Position

def search(list,n):

    l = 0
    u = len(list) - 1

    while l <= u:
        mid = (l+u)//2  # // repr integer division
        if list[mid] == n:
            globals() ['pos'] = mid
            return True
        else:
            if list[mid] < n:
                l = mid + 1
            else:
                u = mid - 1
    return False

list = [2,3,5,6,8,9]       # here list is created.


n = 1   # here is the value we are going to Search

if search(list,n):
    print("Found at ", pos)
else:
    print("Not Found")

