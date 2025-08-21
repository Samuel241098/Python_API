nums = [5, 2, 8, 1, 9]
print(sorted(nums))
for i in range(len(nums)):
    #print(i)
    for j in range(i+1,len(nums)):
        print(j)
        if nums[i]>nums[j]:
            nums[i],nums[j] = nums[j],nums[i]
print(nums)
