# Scenario :
# if the element in the list or not in the list.
# Searching for a value in the list

pos = -1      # Position
def search(list,n):
    i = 0
    while i < len(list):
        if list[i] == n:
            globals() ['pos'] = i     # Accessing the global variable
            return True
        i = i + 1
    return False


list = [2,3,5,6,8,9]  # here list is created.

n = 6   # here is the value we are going to Search

if search(list,n):
    print("Found at ", pos)
else:
    print("Not Found")