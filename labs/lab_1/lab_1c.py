"""
lab_1c.py

Given a list of numbers, return the maximum sum of any contiguous subarray of the list.

Do not assume anything. Account for all edge cases.

Derived from LeetCode problem: https://leetcode.com/problems/maximum-subarray/ (leetcode medium)
"""

# TODO: Find and resolve the bug in the following implementation. Create unit tests to verify your fix.
def max_subarray_sum(nums: list[int]) -> int:
    """
    Function that takes in a list of integers and returns the maximum sum of any contiguous subarray.

    Args:
        nums (list[int]): List of integers.

    Returns:
        int: The maximum sum of any contiguous subarray.
    """

    if not nums:
        raise ValueError("List cannot be empty")
    
    max_current = max_global = nums[0]
    
    for num in nums[1:]:
        max_current = max(num, max_current + num)
        if max_current > max_global:
            max_global = max_current
            
    return max_global

# Example usage:
def main1():
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    result = max_subarray_sum(nums)
    print(f"Maximum subarray sum: {result}")

assert max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]) == 6  # [4,-1,2,1] has the largest sum = 6
assert max_subarray_sum([1]) == 1  # Single element array
assert max_subarray_sum([-1]) == -1  # Single negative element array
assert max_subarray_sum([-2, -3, -1]) == -1  # All negative elements, should return the least negative number
assert max_subarray_sum([5, 4, -1, 7, 8]) == 23  # [5, 4, -1, 7, 8] has the largest sum = 23

def main2():
    nums = [2,-2,1,4,-2,-1,3,-2,0]
    result = max_subarray_sum(nums)
    print(f"Maximum subarray sum: {result}")

if __name__ == "__main__":
    main1()
    main2()