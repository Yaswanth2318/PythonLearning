def sort(nums):

    for i in range(5):  # range(5) low index to high index
        minpos = i
        for j in range(i,6):   #range(i,6) go till 5(inner_loop)
            if nums[j] < nums[minpos]:
                minpos = j

        temp = nums[i]   # in Selection_sort we swap only once and its become outerloop, so here we swap 'i' i.e., outer_loop.
        nums[i] = nums[minpos]
        nums[minpos] = temp

        print(nums)


nums = [2,3,9,6,0,4]
sort(nums)
print(nums)
