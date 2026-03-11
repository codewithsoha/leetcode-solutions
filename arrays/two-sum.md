# Two Sum

## Problem
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

## Approach
Use a hashmap (dictionary) to store numbers and their indices while iterating through the array.  
For each element, check if the complement (target - number) already exists in the hashmap.

## Time Complexity
O(n)

## Space Complexity
O(n)
## Python Solution

class Solution(object):
    def twoSum(self, nums, target):
        num_map = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in num_map:
                return [num_map[complement], i]

            num_map[nums[i]] = i



nums = [2, 7, 11, 15]
target = 9

sol = Solution()
result = sol.twoSum(nums, target)

print(result) 
