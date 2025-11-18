def twoSum(nums, target):
    number = len(nums)
    for i in range(number):
        for n in range(i + 1, number):
            if nums[i] + nums[n] == target:
                return [i, n]
    return 'Нужные индексы не найдены!'

print(twoSum([1,2,3,4,5,6,7,8], 9))

