

f = open('MyData','r') # Opening a file (r = read).


# Read a file
# print(f.read())          # read a file
# print(f.readline(4),end = "")   # reads a characters(4) of aline
# print(f.readline())   #Reads a line in a file.

# Write a file
f1 = open('abc','w')  #its writes(its first checks and creates a file)  the file in a Project (w= write)
f1.write('Something')

f1 = open('abc','a')   #append toa file
f1.write(' Yash')

for data in f:
    f1.write(data)

f1 = open('abc','rb')  # read a binary file (ex : img)
f1 = open('abc','wb')  # Write a binary file.





