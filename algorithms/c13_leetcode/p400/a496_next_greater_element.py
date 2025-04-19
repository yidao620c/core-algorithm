# -*- encoding: utf-8 -*-
"""
496. 下一个更大元素 I
nums1中数字x的下一个更大元素是指x在nums2中对应位置右侧的第一个比x大的元素。

给你两个没有重复元素的数组nums1和nums2，下标从0开始计数，其中nums1是nums2的子集。

对于每个 0 <= i < nums1.length ，找出满足 nums1[i] == nums2[j] 的下标 j ，
并且在nums2确定nums2[j]的下一个更大元素。如果不存在下一个更大元素，那么本次查询的答案是-1 。

返回一个长度为nums1.length的数组 ans 作为答案，满足ans[i]是如上所述的下一个更大元素。

输入：nums1 = [4,1,2], nums2 = [1,3,4,2].
输出：[-1,3,-1]
解释：nums1 中每个值的下一个更大元素如下所述：
- 4 ，nums2 = [1,3,4,2]。不存在下一个更大元素，所以答案是 -1 。
- 1 ，nums2 = [1,3,4,2]。下一个更大元素是 3 。
- 2 ，nums2 = [1,3,4,2]。不存在下一个更大元素，所以答案是 -1 。

输入：nums1 = [2,4], nums2 = [1,2,3,4].
输出：[3,-1]
解释：nums1 中每个值的下一个更大元素如下所述：
- 2 ，nums2 = [1,2,3,4]。下一个更大元素是 3 。
- 4 ，nums2 = [1,2,3,4]。不存在下一个更大元素，所以答案是 -1。

进阶：你可以设计一个时间复杂度为 O(nums1.length + nums2.length) 的解决方案吗？

算法思路：
这个问题可以这样抽象思考：把数组的元素想象成并列站立的人，元素大小想象成人的身高。这些人面对你站成一列，
如何求元素「2」的 Next Greater Number 呢？很简单，如果能够看到元素「2」，
那么他后面可见的第一个人就是「2」的 Next Greater Number，因为比「2」小的元素身高不够，都被「2」挡住了，
第一个露出来的就是答案。

单调栈解决问题的模板。for 循环要从后往前扫描元素，因为我们借助的是栈的结构，倒着入栈，
其实是正着出栈。while 循环是把两个“高个”元素之间的元素排除，因为他们的存在没有意义，前面挡着个“更高”的元素，
所以他们不可能被作为后续进来的元素的 Next Great Number 了。

这个算法的时间复杂度不是那么直观，如果你看到 for 循环嵌套 while 循环，可能认为这个算法的复杂度也是 O(n^2)，
但是实际上这个算法的复杂度只有 O(n)。

分析它的时间复杂度，要从整体来看：总共有 n 个元素，每个元素都被 push 入栈了一次，而最多会被 pop 一次，
没有任何冗余操作。所以总的计算规模是和元素规模 n 成正比的，也就是 O(n) 的复杂度。

先用单调栈找到nums2每个元素对应的下个最大元素，然后装入Map中。后面对于num1的求值直接从Map中获取。
"""
from typing import List


class LinkedNode:
    def __init__(self, val_, next_=None):
        self.val = val_
        self.next = next_

    def __str__(self):
        return str(self.val)


class LinkedStack:
    def __init__(self):
        self.first = None

    def push(self, val):
        self.first = LinkedNode(val, self.first)

    def pop(self):
        if not self.first:
            return None
        res = self.first.val
        self.first = self.first.next
        return res

    def peek(self):
        if not self.first:
            return None
        return self.first.val

    def empty(self):
        return self.first is None


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2_size = len(nums2)
        nums2_map = {}  # 存放num2的单调栈
        count = 0
        stack = LinkedStack()  # 存放高个元素的栈
        for item in nums2[::-1]:
            while not stack.empty() and nums2[nums2_size - 1 - count] > stack.peek():
                stack.pop()  # 把中间小的数剔除掉
            nums2_map[item] = -1 if stack.empty() else stack.peek()
            stack.push(item)  # 然后再把这个数入栈，接受后面的身高判定
            count += 1
        return [nums2_map[i] for i in nums1]


if __name__ == '__main__':
    ans = Solution().nextGreaterElement([4, 1, 2], [1, 3, 4, 2])
    print(ans)
