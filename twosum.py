class Solution():
    def twoSum(self,nums,target):

        num_map={}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return[num_map[complement],i]
            num_map[num] = i
nums =[2,7,11,15]
target = 9
solution = Solution()
result = solution.twoSum(nums,target)
print(f"Indices of numbers add up to {target} are : {result}")
