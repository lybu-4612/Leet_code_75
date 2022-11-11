def two_sum(nums,target):
    dict = {}
    for idx, val in enumerate(nums):
        if target -  val in dict:
            return [dict[target - val], idx]
        else:
            dict[val] = idx
    
    
print(two_sum([2,7,11,15],9))
