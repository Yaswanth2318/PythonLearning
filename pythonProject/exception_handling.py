a = 5
b = 0

try:
    print("resource open")
    print(a/b) # here statement is resource   #need to learn exception names.

except ZeroDivisionError:
    print("invalid output")
except Exception as e:               # we can give except, when we want to print the error as we want.
    print("cannot divisible by zero",e)

finally:
    print("resource closed")


