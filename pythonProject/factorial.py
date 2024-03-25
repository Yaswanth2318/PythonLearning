
# def fact(n):
#
#     f = 1
#
#     for i in range(1,n+1):
#         f = f*i
#
#     return f
#
# n = 10
# result = fact(n)
# print(result)

# Recursion
# import sys
# sys.setrecursionlimit(3000)
# print(sys.getrecursionlimit())
# i = 0
# def greet():
#     global i
#     i+=1
#
#     print("hello",i)
#     greet()
# greet()



#factorial
# def fact(n):
#
#     if n ==0 :
#         return 1
#     return n * fact(n-1)
# n = int(input("enter the factorial number:"))
# result = fact(n)
# print(result)