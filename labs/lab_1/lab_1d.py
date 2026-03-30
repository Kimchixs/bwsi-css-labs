"""
lab_1d.py

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Derived from LeetCode problem: https://leetcode.com/problems/two-sum/ (leetcode easy)
"""


def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Function that takes in a list of integers and a target integer, and returns the indices of the two numbers that add up to the target.

    Args:
        nums (list[int]): List of integers.
        target (int): Target integer.
    
    Returns:
        list[int]: Indices of the two numbers that add up to the target.
    """

    num_to_index = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], index]
        num_to_index[num] = index
    return []  # In case there is no solution, though the problem guarantees one exists.

# Example usage:
def main1():
    nums = [2, 7, 11, 15]
    target = 9
    result = two_sum(nums, target)
    print(f"Indices of the two numbers that add up to {target}: {result}")

assert two_sum([2, 7, 11, 15], 9) == [0, 1]  # nums[0] + nums[1] = 2 + 7 = 9
assert two_sum([3, 2, 4], 6) == [1, 2]  # nums[1] + nums[2] = 2 + 4 = 6
assert two_sum([3, 3], 6) == [0, 1]  # nums[0] + nums[1] = 3 + 3 = 6
assert two_sum([1, 2, 3, 4, 5], 9) == [3, 4]  # nums[3] + nums[4] = 4 + 5 = 9

def main2():
    nums = [1, 2, 3, 4, 5]
    target = 9
    result = two_sum(nums, target)
    print(f"Indices of the two numbers that add up to {target}: {result}")

if __name__ == "__main__":
    main1()
    main2()