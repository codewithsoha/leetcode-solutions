Contains Duplicate
Problem Statement
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
Example
Input
nums = [1,2,3,1]
Output
true
Explanation
The number 1 appears more than once in the array.
Approach
To solve this problem efficiently, we use a set data structure.
A set stores only unique elements, so it helps us quickly check whether a number has already appeared in the array.
Steps:
Create an empty set called seen.
Traverse each element in the array.
If the current element already exists in the set, it means a duplicate is found, so return True.
Otherwise, add the element to the set.
If the loop finishes without finding duplicates, return False.
This approach avoids nested loops and keeps the solution efficient.

CODE

class Solution:
    def containsDuplicate(self, nums):
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False


nums = [1,2,3,1]

sol = Solution()
print(sol.containsDuplicate(nums))



Complexity Analysis
Time Complexity:
O(n) – We traverse the array once.
Space Complexity:
O(n) – We store elements in a set.
