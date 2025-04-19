# -*- encoding: utf-8 -*-
"""
283. 移动零
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
请注意 ，必须在不复制数组的情况下原地对数组进行操作。
输入: nums = [0,1,0,3,12]
输出: [1,3,12,0,0]
输入: nums = [0]
输出: [0]

解题思路：
快慢指针，慢指针保留所有非0值，快指针遍历完数组。最后将慢指针后面的值全部赋值为0即可
"""
from typing import List, NoReturn


class Solution:
    def moveZeroes(self, nums: List[int]) -> NoReturn:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow, fast = 0, 0
        while fast < len(nums):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        while slow < len(nums):
            nums[slow] = 0
            slow += 1
