def containsDuplicate(nums):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]==nums[j]:
                return True
    else:
        return False
nums = [1,2,3,1]
print(containsDuplicate(nums))
