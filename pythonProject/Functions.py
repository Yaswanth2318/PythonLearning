# def greet():
#     print("hello")
# greet()

#pass by value :
# def update(x):
#     x=8
#     print(x)
# a=10
# update(a)
# print(a)

#pass by reference

# def update(lst):
#     print(id(lst))
#     lst[1] = 25
#     print(id(lst))
#     print("x ",lst)
#
# lst = [12,20,30]
# print(id(lst))
# update(lst)
# print(lst)

#position arguments
#
# def person(name,age):
#     print('name',name)
#     print('age',age)
# person('yash',24)

#keyword arguments
# def person(name,age):
#     print('name',name)
#     print('age',age)
# person(name = 'yash',age = 24)


# #Default argument
# def person(name,age =18):
#     print('name',name)
#     print('age',age)
# person(name = 'yash')

#variable length

# def sum(a,*b):
#     c=a
#     for i in b:
#         c=c+i
#     print(c)
# sum(1,2,3,5)

#kwargs
# def person(name, **data):
#     print(name)
#     for i,j in data.items():
#         print(i,j)
#
# person('Yash',age= 28,city = 'nandyal', phone = 987656789)

#local and global variable
# a = 20
# def fun():
#     a = 9
#     x= globals()['a']
#
#     print('in fun',a)
#     x = globals()['a'] = 17 # using globals() we can access both local and global variables.
#
# fun()
#
# print("outside" ,a)

# Examples:

# names = input("Enter the names :" )
# def count(names):
#     for i in names:
#         if len(i) >= 5:
#             return names
#
#     return #pending
#
# count(names)




