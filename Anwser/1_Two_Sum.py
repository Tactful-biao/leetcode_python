'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

'''
通过 (加数1 + 加数2 = 和) 这个式子

把 （和 - 加数1） 得到的结果保存到字典里当成字典的key

如果在找到一个数等于这个key,则说明找到了另一个加数

把两个加数的索引分别返回即可
'''

class Solution:
    def twoSum(self, nums, target):
    	temp = {}
    	lens = len(nums)
    	for i in range(lens):
    		if nums[i] in temp:
    			return [temp[nums[i]], i]
    		temp[target - nums[i]] = i


solution = Solution()
print(solution.twoSum([3,2,11,5,7], 9))