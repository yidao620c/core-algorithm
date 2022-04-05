# -*- encoding: utf-8 -*-
"""
215. 数组中的第K个最大元素

给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。
请注意，你需要找的是数组排序后的第k个最大的元素，而不是第k个不同的元素。

输入: [3,2,1,5,6,4] 和 k = 2
输出: 5

输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4

算法思路：
采用快排的分治思想。我们选择数组区间 A[0...n-1]的最后一个元素 A[n-1]作为 pivot，
对数组 A[0...n-1]原地分区，左边大右边小。分区完成后数组就分成了三部分，A[0...p-1]、A[p]、A[p+1...n-1]。
如果 p+1=K，那 A[p]就是要求解的元素；
如果 p+1<K, 说明第 K 大元素出现在右边 A[p+1...n-1]区间，
如果 p+1>K，说明第 K 大元素出现在左边 A[0...p-1]区间。
我们再按照上面的思路递归地在 A[p+1...n-1] 或者A[0...p-1]区间内存查找。
"""
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.recursive_choose_pivot(nums, 0, len(nums) - 1, k)

    def recursive_choose_pivot(self, nums: List[int], start, end, k: int) -> int:
        while start <= end:
            pivot = self.choose_pivot_by_last(nums, start, end)
            if pivot + 1 == k:
                return nums[pivot]
            if pivot + 1 < k:
                return self.recursive_choose_pivot(nums, pivot + 1, end, k)
            else:
                return self.recursive_choose_pivot(nums, start, pivot - 1, k)

    def choose_pivot_by_last(self, nums: List[int], start, end) -> int:
        pivot_value = nums[end]  # 将最后一个元素定为pivot
        i = start - 1  # 以退为进，初始值设置为start-1
        for j in range(start, end):
            if nums[j] >= pivot_value:  # 将大的数放左边
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1], nums[end] = nums[end], nums[i + 1]
        return i + 1


if __name__ == '__main__':
    res = Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2)
    assert res == 5
