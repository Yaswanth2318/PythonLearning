def topten():

    n = 1

    while n <= 10:
        sq = n*n
        yield sq
        n += 1



values = topten()

# print(values.__next__())
# print(next(values))

for i in values:
    print(i)